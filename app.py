import os
from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route("/")
def home():
    today = date.today()
    target = date(2025, 9, 26)
    days_remaining = (target - today).days
    return render_template("index.html", days=days_remaining)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)