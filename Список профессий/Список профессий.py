from flask import Flask, render_template

app = Flask(__name__)

professions = """инженер-исследователь, пилот, строитель, экзобиолог, 
врач, инженер по терраформированию, климатолог, специалист по радиационной
 защите, астрогеолог, гляциолог, инженер жизнеобеспечения, метеоролог,
  оператор марсохода, киберинженер, штурман, пилот дронов""".split(", ")


@app.route("/list_prof/<list>")
def funk_1(list):
    return render_template("Список профессий.html", prof=professions, par=list)

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1", debug=True)