from flask import Flask, render_template_string, jsonify
from datetime import datetime

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DevOps App</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            text-align: center;
            background: rgba(0,0,0,0.3);
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }

        p {
            font-size: 1.2rem;
            margin: 10px 0;
        }

        .status {
            margin-top: 20px;
            padding: 10px 20px;
            background: #00c853;
            border-radius: 20px;
            display: inline-block;
            font-weight: bold;
        }

        .footer {
            margin-top: 20px;
            font-size: 0.9rem;
            opacity: 0.8;
        }

        button {
            margin-top: 20px;
            padding: 10px 20px;
            border: none;
            border-radius: 20px;
            background: #ff9800;
            color: white;
            font-size: 1rem;
            cursor: pointer;
        }

        button:hover {
            background: #e68900;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>🚀 DevOps Deployment Successful</h1>
    <p>Your app is running on a <b>Self-Hosted Runner</b></p>

    <div class="status">STATUS: UP ✅</div>

    <p>Server Time: {{ time }}</p>

    <button onclick="checkHealth()">Check Health API</button>

    <p id="health-result"></p>

    <div class="footer">
        Built with Flask + Docker + GitHub Actions
    </div>
</div>

<script>
function checkHealth() {
    fetch('/health')
        .then(res => res.json())
        .then(data => {
            document.getElementById("health-result").innerText =
                "Health API → " + JSON.stringify(data);
        })
        .catch(err => {
            document.getElementById("health-result").innerText =
                "Error calling API";
        });
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE, time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "service": "python-app",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
