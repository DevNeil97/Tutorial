from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", content = ["Nirmal", "Tim", "Hello"])

if __name__ == "__main__":
    app.run()
