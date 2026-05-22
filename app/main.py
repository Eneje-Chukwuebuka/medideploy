from flask import Flask, jsonify
from app.config import get_config

app = Flask(__name__)
app.config.from_object(get_config())


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/vitals")
def vitals():
    return jsonify({
        "heart_rate": 72,
        "blood_pressure": "120/80",
        "temperature_celsius": 36.6,
        "environment": app.config.get("ENV_NAME", "unknown")
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
