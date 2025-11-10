from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
JSON_SERVER_URL = "http://localhost:5000/devices"

@app.route("/")
def home():
    devices = requests.get(JSON_SERVER_URL).json()
    return render_template("index.html", devices=devices)

@app.route("/toggle", methods=["POST"])
def toggle_device():
    data = request.get_json()
    device_id = data["id"]
    status = data["status"]

    # Update on JSON Server (cloud simulation)
    update_data = {"status": status}
    requests.patch(f"{JSON_SERVER_URL}/{device_id}", json=update_data)
    return jsonify({"message": "Device updated successfully"})

if __name__ == "__main__":
    app.run(debug=True)
