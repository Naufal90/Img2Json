import os
import json
import cv2
import numpy as np

DATA_DIR = "data"
JSON_DIR = "json"

os.makedirs(JSON_DIR, exist_ok=True)

def convert_image_to_blocks(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape
    blocks = []

    for y in range(height):
        row = []
        for x in range(width):
            pixel = img[y, x]
            if pixel < 128:
                row.append("stone")  # Ubah sesuai blok Minecraft
            else:
                row.append("air")
        blocks.append(row)

    return {
        "filename": os.path.basename(image_path),
        "width": width,
        "height": height,
        "blocks": blocks
    }

image_files = [f for f in os.listdir(DATA_DIR) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
output = [convert_image_to_blocks(os.path.join(DATA_DIR, img)) for img in image_files]

output_path = os.path.join(JSON_DIR, "building.json")
with open(output_path, "w") as json_file:
    json.dump(output, json_file, indent=4)

print(f"Konversi selesai! File JSON tersimpan di {output_path}")
