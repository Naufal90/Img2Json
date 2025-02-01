import os
import json
from PIL import Image
import base64

# Direktori input dan output
DATA_DIR = "../data"
JSON_DIR = "../json"

# Pastikan folder output ada
os.makedirs(JSON_DIR, exist_ok=True)

# Fungsi untuk mengonversi gambar ke JSON
def convert_image_to_json(image_path):
    with open(image_path, "rb") as img_file:
            base64_str = base64.b64encode(img_file.read()).decode("utf-8")
                
                    return {
                            "filename": os.path.basename(image_path),
                                    "base64": base64_str
                                        }

                                        # Proses semua gambar di folder data
                                        image_files = [f for f in os.listdir(DATA_DIR) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

                                        output = []
                                        for image_file in image_files:
                                            image_path = os.path.join(DATA_DIR, image_file)
                                                output.append(convert_image_to_json(image_path))

                                                # Simpan hasil ke JSON
                                                output_path = os.path.join(JSON_DIR, "images.json")
                                                with open(output_path, "w") as json_file:
                                                    json.dump(output, json_file, indent=4)

                                                    print(f"Konversi selesai! File JSON tersimpan di {output_path}")