from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/distribution")
def funk():
    data = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]
    return render_template("По каютам.html", astr=data)

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1", debug=True)