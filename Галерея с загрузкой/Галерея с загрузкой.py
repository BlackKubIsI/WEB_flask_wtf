from crypt import methods
from flask import Flask, render_template, request

app = Flask(__name__)

ph = ["../static/img/1.jpg", "../static/img/2.jpg", "../static/img/3.jpg", "../static/img/4.jpg", "../static/img/5.jpg", "../static/img/6.jpg"]

@app.route("/", methods=["GET", "POST"])
def funk_1():
    if request.method == "POST":
        ph.append("../static/img/" + str(request.form["file"]))
        print(ph)
    return render_template("Галерея с загрузкой.html", photos=ph)

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1", debug=True)




