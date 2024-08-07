from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("tutorial2/index.html")

@app.route("/about")
def about():
    return render_template("tutorial3/about.html")

if __name__ == "__main__":
    app.run(debug=True)