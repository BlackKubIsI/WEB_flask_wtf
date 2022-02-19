from flask import Flask, render_template, request
import random
import json

app = Flask(__name__)

@app.route("/member")
def funk():
    with open("templates/crew.json") as f:
        cosm = random.choice(json.load(f))
    return render_template("Личная карточка.html", astronaut=cosm)

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1", debug=True)