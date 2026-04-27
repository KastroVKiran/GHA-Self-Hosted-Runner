from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 App deployed using Self-Hosted Runner!"

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
