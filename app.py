from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "message": "Python Docker DevOps App is running!"
    })

@app.get("/health")
def health():
    return jsonify({
        "status": "OK"
    })

@app.get("/api/users")
def users():
    return jsonify([
        {"id": 1, "name": "Sateesh"},
        {"id": 2, "name": "DevOps Student"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)