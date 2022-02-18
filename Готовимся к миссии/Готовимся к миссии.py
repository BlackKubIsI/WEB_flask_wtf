from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<title>")
@app.route("/index/<title>")
def funk_1(title):
    return render_template("Готовимся к миссии.html", title=title)

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1", debug=True)