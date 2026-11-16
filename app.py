import os
import uuid
import shutil
import json
import traceback
from typing import Optional

from dotenv import load_dotenv
from flask import Flask, request, jsonify, send_from_directory, make_response
from flask_cors import CORS

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as kimage

import psycopg2
from psycopg2.extras import RealDictCursor

from openai import OpenAI

# ================= LOAD ENV =================
load_dotenv()

# ================= CONFIG =================
MODEL_PATH = os.getenv("MODEL_PATH", "TaxoBloom_model.h5")
STATIC_DIR = "static"
UPLOAD_DIR = "tmp_uploads"
DIAGRAM_DIR = "static/diagrams"

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "bmp"}
IMG_SIZE = 224

PG_HOST = os.getenv("PG_HOST")
PG_DB = os.getenv("PG_DB")
PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")
PG_PORT = os.getenv("PG_PORT")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=OPENAI_API_KEY) if (OPENAI_API_KEY and OPENAI_API_KEY != "your_openai_api_key_here") else None

# ================= SETUP =================
os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(DIAGRAM_DIR, exist_ok=True)

with open("class_names.json", "r", encoding="utf-8") as f:
    CLASS_NAMES = json.load(f)

app = Flask(__name__, static_folder=STATIC_DIR, static_url_path="/static")
CORS(app)

print("[INFO] Loading ML model...")
model = load_model(MODEL_PATH)
print("[INFO] Model loaded.")

# ================= HELPERS =================
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(path):
    img = kimage.load_img(path, target_size=(IMG_SIZE, IMG_SIZE))
    arr = kimage.img_to_array(img) / 255.0
    return np.expand_dims(arr, axis=0)

def get_db_connection():
    return psycopg2.connect(
        host=PG_HOST,
        database=PG_DB,
        user=PG_USER,
        password=PG_PASS,
        port=PG_PORT
    )

def convert_image_path(val: Optional[str]):
    if not val:
        return None
    if val.startswith(("http://", "https://")):
        return val
    filename = os.path.basename(val)
    dst = os.path.join(DIAGRAM_DIR, filename)
    if os.path.exists(val) and not os.path.exists(dst):
        shutil.copy(val, dst)
    return f"/static/diagrams/{filename}" if os.path.exists(dst) else None

# Fallback botanical catalog for the 10 supported classes
FALLBACK_TAXONOMY = {
    "calotropis": {
        "flower_name": "Calotropis",
        "scientific_name": "Calotropis gigantea",
        "kingdom": "Plantae",
        "division": "Tracheophytes",
        "flower_class": "Magnoliopsida",
        "flower_order": "Gentianales",
        "flower_family": "Apocynaceae",
        "genus": "Calotropis",
        "species": "C. gigantea",
        "floral_formula": "⊕ ⚥ K₅ C₍₅₎ A₅ G₍₂₎",
        "floral_diagram": "/static/diagrams/calotropis_floral_diagram.svg"
    },
    "clitoria": {
        "flower_name": "Clitoria",
        "scientific_name": "Clitoria ternatea",
        "kingdom": "Plantae",
        "division": "Tracheophytes",
        "flower_class": "Magnoliopsida",
        "flower_order": "Fabales",
        "flower_family": "Fabaceae",
        "genus": "Clitoria",
        "species": "C. ternatea",
        "floral_formula": "% ⚥ K₍₅₎ C₁₊₂₊₍₂₎ A₍₉₎₊₁ G₁",
        "floral_diagram": "/static/diagrams/clitoria_floral_diagram.svg"
    },
    "crinum": {
        "flower_name": "Crinum",
        "scientific_name": "Crinum asiaticum",
        "kingdom": "Plantae",
        "division": "Tracheophytes",
        "flower_class": "Liliopsida",
        "flower_order": "Asparagales",
        "flower_family": "Amaryllidaceae",
        "genus": "Crinum",
        "species": "C. asiaticum",
        "floral_formula": "⊕ ⚥ P₍₃₊₃₎ A₃₊₃ G₍₃₎",
        "floral_diagram": "/static/diagrams/crinum_floral_diagram.svg"
    },
    "hibiscus": {
        "flower_name": "Hibiscus",
        "scientific_name": "Hibiscus rosa-sinensis",
        "kingdom": "Plantae",
        "division": "Tracheophytes",
        "flower_class": "Magnoliopsida",
        "flower_order": "Malvales",
        "flower_family": "Malvaceae",
        "genus": "Hibiscus",
        "species": "H. rosa-sinensis",
        "floral_formula": "⊕ ⚥ Epk₅₋₈ K₍₅₎ C₅ A₍∞₎ G₍₅₎",
        "floral_diagram": "/static/diagrams/hibiscus_floral_diagram.svg"
    },
    "ixora": {
        "flower_name": "Ixora",
        "scientific_name": "Ixora coccinea",
        "kingdom": "Plantae",
        "division": "Tracheophytes",
        "flower_class": "Magnoliopsida",
        "flower_order": "Gentianales",
        "flower_family": "Rubiaceae",
        "genus": "Ixora",
        "species": "I. coccinea",
        "floral_formula": "⊕ ⚥ K₍₄₎ C₍₄₎ A₄ G₍₂₎",
        "floral_diagram": "/static/diagrams/ixora_floral_diagram.svg"
    },
    "lotus": {
        "flower_name": "Lotus",
        "scientific_name": "Nelumbo nucifera",
        "kingdom": "Plantae",
        "division": "Tracheophytes",
        "flower_class": "Magnoliopsida",
        "flower_order": "Proteales",
        "flower_family": "Nelumbonaceae",
        "genus": "Nelumbo",
        "species": "N. nucifera",
        "floral_formula": "⊕ ⚥ K₂₋₄ C∞ A∞ G_∞",
        "floral_diagram": "/static/diagrams/lotus_floral_diagram.svg"
    },
    "sunflower": {
        "flower_name": "Sunflower",
        "scientific_name": "Helianthus annuus",
        "kingdom": "Plantae",
        "division": "Tracheophytes",
        "flower_class": "Magnoliopsida",
        "flower_order": "Asterales",
        "flower_family": "Asteraceae",
        "genus": "Helianthus",
        "species": "H. annuus",
        "floral_formula": "Ray: % ♀ K_pappus C₍₅₎ A₀ G₍₂₎ | Disc: ⊕ ⚥ K_pappus C₍₅₎ A₍₅₎ G₍₂₎",
        "floral_diagram": "/static/diagrams/sunflower_floral_diagram.svg"
    },
    "tridax": {
        "flower_name": "Tridax",
        "scientific_name": "Tridax procumbens",
        "kingdom": "Plantae",
        "division": "Tracheophytes",
        "flower_class": "Magnoliopsida",
        "flower_order": "Asterales",
        "flower_family": "Asteraceae",
        "genus": "Tridax",
        "species": "T. procumbens",
        "floral_formula": "⊕ ⚥ K_pappus C₍₅₎ A₍₅₎ G₍₂₎",
        "floral_diagram": "/static/diagrams/tridax_floral_diagram.svg"
    },
    "periwinkle": {
        "flower_name": "Periwinkle",
        "scientific_name": "Catharanthus roseus",
        "kingdom": "Plantae",
        "division": "Tracheophytes",
        "flower_class": "Magnoliopsida",
        "flower_order": "Gentianales",
        "flower_family": "Apocynaceae",
        "genus": "Catharanthus",
        "species": "C. roseus",
        "floral_formula": "⊕ ⚥ K₅ C₍₅₎ A₅ G₍₂₎",
        "floral_diagram": "/static/diagrams/periwinkle_floral_diagram.svg"
    },
    "rose": {
        "flower_name": "Rose",
        "scientific_name": "Rosa indica",
        "kingdom": "Plantae",
        "division": "Tracheophytes",
        "flower_class": "Magnoliopsida",
        "flower_order": "Rosales",
        "flower_family": "Rosaceae",
        "genus": "Rosa",
        "species": "R. indica",
        "floral_formula": "⊕ ⚥ K₅ C₅ A∞ G∞",
        "floral_diagram": "/static/diagrams/rose_floral_diagram.svg"
    }
}

FALLBACK_DESCRIPTIONS = {
    "calotropis": "Calotropis gigantea (Crown Flower) is a large shrub with clusters of waxy flowers with a distinct crown-like center. Native to tropical Asia, it has wide traditional Ayurvedic uses.",
    "clitoria": "Clitoria ternatea (Butterfly Pea) is a tropical vine with striking deep-blue papilionaceous flowers. Celebrated for high antioxidant anthocyanins and beneficial nitrogen fixation.",
    "crinum": "Crinum asiaticum (Grand Crinum / Spider Lily) is a perennial bulbous monocot with large umbels of sweetly scented white flowers with narrow spreading petals.",
    "hibiscus": "Hibiscus rosa-sinensis (China Rose) features large, vibrant trumpet-shaped flowers with prominent staminal columns extending beyond the petals. Commonly studied for actinomorphic symmetry.",
    "ixora": "Ixora coccinea (Jungle Flame) is an evergreen tropical shrub known for its dense corymb clusters of bright scarlet, tubular blossoms.",
    "lotus": "Nelumbo nucifera (Sacred Lotus) is an aquatic perennial with fragrant pink or white flowers and a unique self-cleaning leaf surface ('Lotus effect') bearing spiritual and cultural significance.",
    "sunflower": "Helianthus annuus (Common Sunflower) has a prominent composite flower head (pseudanthium) comprising hundreds of individual ray and disc florets that turn toward the sun.",
    "tridax": "Tridax procumbens (Coatbuttons) is a daisy-like medicinal herb featuring three-toothed ray florets and yellow disc florets. Known in ethnobotany for rapid wound healing.",
    "periwinkle": "Catharanthus roseus (Madagascar Periwinkle) bears five-petaled salverform blooms. It is celebrated pharmacologically for vinca alkaloids used in modern oncology.",
    "rose": "Rosa indica is a woody perennial shrub celebrated for fragrant multi-layered petals and hips rich in vitamin C. It is one of the most culturally revered flowers worldwide."
}

def fetch_taxonomy(name):
    clean_name = name.lower().strip()
    fallback = FALLBACK_TAXONOMY.get(clean_name, {}).copy()

    # Try PostgreSQL first if active
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("""
            SELECT flower_name, scientific_name, kingdom, division,
                   flower_class, flower_family, flower_order,
                   genus, species, floral_formula, floral_diagram
            FROM taxobloom
            WHERE LOWER(flower_name)=LOWER(%s)
            LIMIT 1
        """, (name,))
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row:
            res = dict(row)
            # Ensure floral_diagram always uses authentic verified diagram SVG and not a formula screenshot
            diagram_val = res.get("floral_diagram")
            if not diagram_val or "Screenshot" in str(diagram_val) or str(diagram_val).endswith(".png"):
                res["floral_diagram"] = fallback.get("floral_diagram")
            else:
                converted = convert_image_path(diagram_val)
                res["floral_diagram"] = converted if converted else fallback.get("floral_diagram")

            # If DB stored a screenshot for formula, prefer the clean unicode formula text from fallback
            formula_val = res.get("floral_formula")
            if not formula_val or "Screenshot" in str(formula_val) or str(formula_val).endswith((".png", ".jpg")):
                res["floral_formula"] = fallback.get("floral_formula")

            return res
    except Exception:
        pass

    # Fallback to local verified botanical catalog
    return fallback

def get_llm_description(name):
    if openai_client:
        try:
            rsp = openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a botanist."},
                    {"role": "user", "content": f"Give a short 5-6 line student-friendly educational description of {name} including physical characteristics, habitat, and traditional or medicinal uses."}
                ]
            )
            desc = rsp.choices[0].message.content
            if desc:
                return desc.strip()
        except Exception:
            pass

    return FALLBACK_DESCRIPTIONS.get(name.lower(), f"Botanical specimen profile for {name}.")

# ================= NO-CACHE MIDDLEWARE =================
@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

# ================= ROUTES =================

# ✅ LOGIN (FIRST PAGE)
@app.route("/")
def login_page():
    response = make_response(send_from_directory(STATIC_DIR, "login.html"))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

# ✅ DASHBOARD
@app.route("/dashboard")
def dashboard_page():
    response = make_response(send_from_directory(STATIC_DIR, "dashboard.html"))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

# ✅ PREDICTION PAGE
@app.route("/predict-page")
@app.route("/predict_page")
def predict_page():
    response = make_response(send_from_directory(STATIC_DIR, "index.html"))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

# ✅ ML API
@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    if file.filename == "" or not allowed_file(file.filename):
        return jsonify({"error": "Invalid image"}), 400

    uid = uuid.uuid4().hex
    ext = file.filename.rsplit(".", 1)[1].lower()
    path = os.path.join(UPLOAD_DIR, f"{uid}.{ext}")

    try:
        file.save(path)
        img = preprocess_image(path)

        preds = model.predict(img)[0]
        idx = int(np.argmax(preds))

        label = CLASS_NAMES[idx]
        confidence = float(preds[idx])

        return jsonify({
            "predicted_label": label,
            "confidence": confidence,
            "details": fetch_taxonomy(label),
            "description": get_llm_description(label)
        })

    except Exception:
        traceback.print_exc()
        return jsonify({"error": "Prediction failed"}), 500

    finally:
        if os.path.exists(path):
            os.remove(path)

# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)
