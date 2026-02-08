from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from extractor import extract_fields
from validator import validate_fields
from router import route_claim
import json, os, datetime

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Serve frontend files
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    frontend_dir = os.path.join(os.path.dirname(__file__), "../frontend")
    if path != "" and os.path.exists(os.path.join(frontend_dir, path)):
        return send_from_directory(frontend_dir, path)
    return send_from_directory(frontend_dir, "index.html")

# API endpoint
@app.route("/submit-claim", methods=["POST"])
def submit_claim():
    data = request.json

    extracted = extract_fields(data)
    missing = validate_fields(extracted)
    route, reason = route_claim(extracted, missing)

    result = {
        "extractedFields": extracted,
        "missingFields": missing,
        "recommendedRoute": route,
        "reasoning": reason
    }

    output_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"result_{timestamp}.json"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w") as f:
        json.dump(result, f, indent=4)

    print(f"Claim saved to: {filepath}")

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
