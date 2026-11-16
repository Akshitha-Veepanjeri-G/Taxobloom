# 🌸 TaxoBloom — AI Botanical Classification & Taxonomy Retrieval System

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.13-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15+-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-Modern_Glassmorphism-38B2AC?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)

**TaxoBloom** is an intelligent botanical web platform that combines **Deep Convolutional Neural Networks (CNN)** with **Linnaean Botanical Taxonomy**. By uploading a flower photo, students, researchers, and botanists can immediately classify the specimen, deduce its full biological classification hierarchy, and view floral formulas, floral cross-section diagrams, and AI-generated educational insights.

---

## 🌟 Key Features

- **Deep Learning Flower Classifier**: Pre-trained CNN (`TaxoBloom_model.h5`) accepting $224 \times 224$ RGB image tensors.
- **7-Tier Linnaean Taxonomy Tree**: Retrieves Kingdom, Division, Class, Order, Family, Genus, and Species.
- **Floral Anatomy & Formulas**:
  - Displays symbolic floral formulas (e.g., $\oplus \ \text{\textdied} \ \text{K}_{(5)} \ \text{C}_5 \ \text{A}_{(\infty)} \ \text{G}_{(5)}$).
  - Displays anatomical floral cross-section diagrams with an interactive **Click-to-Zoom Lightbox**.
- **AI Botanist Insights**: Integration with Groq (Llama 3.3) for student-friendly morphological and ethnobotanical reports (with automatic offline fallback).
- **Modern Responsive UI**:
  - Drag-and-drop file upload zone with live image preview and format validation.
  - Dynamic animated confidence gauge and match quality indicator.
  - Persistent **Light & Dark mode** toggle saved across sessions.
  - Interactive **Species Hub** detailing all recognized flowers.

---

## 🌺 Supported Flower Species (10 Classes)

| # | Common Name | Scientific Name | Botanical Family |
|---|-------------|-----------------|------------------|
| 1 | **Calotropis** (Crown Flower) | *Calotropis gigantea* | Apocynaceae |
| 2 | **Clitoria** (Butterfly Pea) | *Clitoria ternatea* | Fabaceae |
| 3 | **Crinum** (Spider Lily) | *Crinum asiaticum* | Amaryllidaceae |
| 4 | **Hibiscus** (China Rose) | *Hibiscus rosa-sinensis* | Malvaceae |
| 5 | **Ixora** (Jungle Flame) | *Ixora coccinea* | Rubiaceae |
| 6 | **Lotus** (Sacred Lotus) | *Nelumbo nucifera* | Nelumbonaceae |
| 7 | **Sunflower** | *Helianthus annuus* | Asteraceae |
| 8 | **Tridax** (Coatbuttons) | *Tridax procumbens* | Asteraceae |
| 9 | **Periwinkle** | *Catharanthus roseus* | Apocynaceae |
| 10 | **Rose** | *Rosa indica* | Rosaceae |

---

## 📁 Project Directory Structure

```text
MiniProject/
├── app.py                  # Main Flask application & ML prediction routes
├── class_names.json        # 10 trained class labels in model index order
├── TaxoBloom_model.h5      # Keras/TensorFlow pre-trained deep learning model
├── extract_labels.py       # Helper script to verify label mapping
├── image_prepare.py        # Utility script for diagram ingestion
├── llm.py                  # Groq/OpenAI LLM prompt generator
├── model.ipynb             # Model training & evaluation notebook
├── requirements.txt        # Python package dependencies
├── .env                    # Environment configuration (DB, API keys, paths)
├── static/                 # Frontend assets & templates
│   ├── login.html          # Authentication portal with demo auto-fill
│   ├── dashboard.html      # Species hub & operations dashboard
│   ├── index.html          # Main drag-and-drop prediction studio
│   └── diagrams/           # Stored floral formulas and cross-section diagrams
└── tmp_uploads/            # Temporary directory for uploaded files during inference
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites
Ensure you have **Python 3.10 to 3.13** installed on your system.

### 2. Install Dependencies
Open PowerShell or your terminal in the project directory:

```powershell
pip install -r requirements.txt
```

*(Note: On systems with multiple Python installations where TensorFlow is in Python 3.13, you can use `py -3.13 -m pip install -r requirements.txt`)*

### 3. Environment Configuration (`.env`)
The project includes a `.env` file for configuration:

```env
MODEL_PATH=TaxoBloom_model.h5
UPLOAD_DIR=tmp_uploads
STATIC_DIR=static

# PostgreSQL (Optional - The app includes offline botanical fallbacks)
PG_HOST=localhost
PG_DB=taxobloom_new
PG_USER=postgres
PG_PASS=your_password_here
PG_PORT=5432

# OpenAI API (Optional - Generates AI botanist descriptions)
OPENAI_API_KEY=your_openai_api_key_here
```

> [!NOTE]
> The app is built with **resilient offline fallbacks**. Even if PostgreSQL or the OpenAI API key is not configured, the app will smoothly display botanical taxonomy, floral formulas, and descriptions without crashing.

### 4. Run the Application

You can run using the project's virtual environment:

```powershell
# Activate the virtual environment (PowerShell)
.\.venv\Scripts\Activate.ps1

# Run the Flask app
python app.py
```

*(Alternatively, run directly without activating: `.\.venv\Scripts\python.exe app.py` or `py -3.13 app.py`)*

The terminal will confirm:
```text
[INFO] Loading ML model...
[INFO] Model loaded.
 * Running on http://127.0.0.1:5000
```

### 5. Access the Web Studio

1. Open your browser and go to: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**
2. Enter the default credentials (or click **⚡ Auto Fill**):
   - **Username:** `admin`
   - **Password:** `1234`
3. Explore the **Dashboard** or proceed directly to the **Prediction Studio**.
4. Drag & drop or browse a flower photo (`.png`, `.jpg`, `.jpeg`, `.bmp`) and click **Predict Flower & Taxonomy**.

---

## 🔌 API Reference

### `POST /predict`
Uploads a flower image for CNN classification and taxonomy lookup.

- **Request:** `multipart/form-data`
  - `image`: Image file binary
- **Response Format (`application/json`):**
```json
{
  "predicted_label": "Hibiscus",
  "confidence": 0.9842,
  "details": {
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
    "floral_diagram": "/static/diagrams/Screenshot 2025-12-09 050110.png"
  },
  "description": "Hibiscus rosa-sinensis is a quintessential solitary bloom with vibrant petals..."
}
```

---

## 🛠️ Technology Stack

- **Model Core:** TensorFlow / Keras (CNN Classifier)
- **Backend Service:** Flask 3.x, Werkzeug, Flask-CORS
- **Database:** PostgreSQL (with `psycopg2-binary`)
- **GenAI Layer:** OpenAI Python SDK (`gpt-4o-mini`)
- **Frontend:** HTML5, Modern Tailwind CSS, Plus Jakarta Sans & Outfit Fonts, Custom Glassmorphism

---

## 📄 License
Academic and educational project use.

