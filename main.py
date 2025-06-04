from flask import Flask, request, jsonify
from ultralytics import YOLO
from PIL import Image
import io
import numpy as np

app = Flask(__name__)

# Carrega o modelo YOLOv8 treinado
model = YOLO("best.pt")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "image" not in request.files:
        return jsonify({"error": "No image file found"}), 400

    file = request.files["image"]
    image = Image.open(io.BytesIO(file.read())).convert("RGB")
    results = model(image)
    detections = results[0].boxes

    # Pega dados das caixas
    boxes = detections.data.cpu().numpy() if detections is not None else []

    return jsonify({
        "cromossomos": len(boxes),
        "boxes": [
            {
                "x1": float(box[0]),
                "y1": float(box[1]),
                "x2": float(box[2]),
                "y2": float(box[3]),
                "confidence": float(box[4])
            } for box in boxes
        ]
    })

@app.route("/", methods=["GET"])
def index():
    return "API de detecção de cromossomos ativa 🚀"

if __name__ == "__main__":
    app.run(debug=True)