from flask import Flask, render_template, request, session
from classes import Perfil, Perfis

app = Flask(__name__)

app.secret_key = "LGBSDGKYW#TBRjGJKikejhrg"


@app.route("/")
def home():
    if "login" not in session:
        session["login"] = False

    return render_template("index.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        if request.form["nome"] == "usuario" and request.form["senha"] == "usuario":
            session["login"] = True
            return render_template("dashboard.html", Perfis=Perfis)
        else:
            return render_template("warning.html")
    elif request.method == "GET" and session["login"] == True:
        return render_template("dashboard.html", Perfis=Perfis)
    else:
        return render_template("warning.html")



@app.route("/logout")
def logout():
    if "login" in session:
        session["login"] = False

    return render_template("index.html")

@app.route("/adicionar")
def adicionar():

    return render_template("dashboard.html", Perfis=Perfis)





if __name__ == '__main__':
    app.run(debug=True)     
