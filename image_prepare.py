# image_prepare.py
import os
import shutil
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

load_dotenv()

DIAGRAM_DIR = os.getenv("DIAGRAM_DIR", "static/diagrams")
os.makedirs(DIAGRAM_DIR, exist_ok=True)

PG_HOST = os.getenv("PG_HOST", "localhost")
PG_DB = os.getenv("PG_DB", "taxobloom")
PG_USER = os.getenv("PG_USER", "postgres")
PG_PASS = os.getenv("PG_PASS", "")
PG_PORT = os.getenv("PG_PORT", "5432")

def get_conn():
    return psycopg2.connect(host=PG_HOST, database=PG_DB, user=PG_USER, password=PG_PASS, port=PG_PORT)

def is_url(s):
    return s and (s.startswith("http://") or s.startswith("https://"))

def download_url(url, dst):
    try:
        resp = requests.get(url, timeout=20)
        resp.raise_for_status()
        with open(dst, "wb") as f:
            f.write(resp.content)
        print("Downloaded", url, "->", dst)
        return True
    except Exception as e:
        print("Failed to download", url, e)
        return False

def prepare():
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT flower_name, floral_formula, floral_diagram FROM taxobloom")
    rows = cur.fetchall()
    for r in rows:
        for key in ("floral_formula", "floral_diagram"):
            val = r.get(key)
            if not val:
                continue
            if is_url(val):
                filename = os.path.basename(urlparse(val).path) or f"{r['flower_name']}_{key}.jpg"
                dst = os.path.join(DIAGRAM_DIR, filename)
                if not os.path.exists(dst):
                    if download_url(val, dst):
                        # optionally: update DB to store filename instead of URL (commented)
                        pass
            else:
                # val is probably local path or filename
                if os.path.exists(val) and os.path.isfile(val):
                    filename = os.path.basename(val)
                    dst = os.path.join(DIAGRAM_DIR, filename)
                    if not os.path.exists(dst):
                        try:
                            shutil.copy2(val, dst)
                            print("Copied", val, "->", dst)
                        except Exception as e:
                            print("Copy failed", val, e)
                else:
                    print("Missing local file for", r['flower_name'], key, ":", val)
    cur.close()
    conn.close()

if __name__ == "__main__":
    prepare()
    print("Done. Check", DIAGRAM_DIR)
