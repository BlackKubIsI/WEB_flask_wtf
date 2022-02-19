from flask import Flask, render_template

app = Flask(__name__)

@app.route("/answer")
@app.route("/auto_answer")
def funk():
    names = ["title", "surname", "name", "education", "profession", "sex", "motivation", "ready"]
    answers = ["анкета", "Wanty", "Mark", "выше среднего", "штурман марсохода", "male", "Всегда мечтал застрять на Марсе!", "True"]
    return render_template("Автоматический ответ.html", NAMES=names, ANSWERS=answers)

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1", debug=True)
