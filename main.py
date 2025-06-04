from flask import Flask, request, jsonify
from ultralytics import YOLO
from PIL import Image
import io

app = Flask(__name__)
model = YOLO("best.pt")

@app.route("/", methods=["GET"])
def home():
    return "API YOLOv8 local está rodando 🚀"

@app.route("/analyze", methods=["POST"])
def analyze():
    if "image" not in request.files:
        return jsonify({"error": "No image file uploaded"}), 400

    file = request.files["image"]
    image = Image.open(io.BytesIO(file.read())).convert("RGB")
    results = model(image)
    boxes = results[0].boxes.data.cpu().numpy()

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