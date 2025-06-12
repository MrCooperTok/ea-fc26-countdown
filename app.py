from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route("/")
def home():
    print(">>> Route reached!")
    today = date.today()
    target = date(2025, 9, 26)
    days_remaining = (target - today).days
    return render_template("index.html", days=days_remaining)

if __name__ == "__main__":
    app.run(debug=True)