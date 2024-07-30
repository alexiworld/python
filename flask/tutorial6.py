from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "FlaskTutorialSecretKey"
app.permanent_session_lifetime = timedelta(minutes=30) #days=5

@app.route("/")
def home():
    return render_template("tutorial5/index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session.permanent = True # required for permanent_session_lifetime to work
        session["user"] = user
        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user")) 
        return render_template("tutorial6/login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("tutorial6/user.html", user=user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have been successfully logged out, {user}!", "info")
    else:
        flash(f"You have been successfully logged out!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)