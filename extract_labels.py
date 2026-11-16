from tensorflow.keras.models import load_model
import json

MODEL_PATH = "TaxoBloom_model.h5"  # change if different

model = load_model(MODEL_PATH)

try:
    labels = model.class_names  # For models trained with ImageDataGenerator (TensorFlow 2.9+)
except:
    try:
        labels = list(model.class_indices.keys())  # If model.class_indices exists
    except:
        labels = None

print("\n🔍 Extracted Labels:", labels)

if labels:
    with open("class_names.json", "w") as f:
        json.dump(labels, f, indent=4)
    print("\n✅ Saved correct label order to class_names.json")
else:
    print("\n❌ Could not detect labels automatically. You MUST manually list class names in correct training order.")
