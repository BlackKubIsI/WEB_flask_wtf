from crypt import methods
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route("/login", methods=["GET", "POST"])
def funk():
    if request.method == "GET":
        return render_template("Двойная защита.html")
    elif request.method == "POST":
        data = ["id_as: " + str(request.form["id_as"]), "pas_as: " + str(request.form["pas_as"]),
        "id_cap: " + str(request.form["id_cap"]), "pas_cap: " + str(request.form["pas_cap"])]
        return "<br>".join(data)

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1", debug=True)