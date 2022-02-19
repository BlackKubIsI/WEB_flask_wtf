from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/table!<male>!<age>")
def funk(male, age):
    age = int(age)
    male = int(male == "male")
    colors = ["#FF69B4", "#C71585", "#FA8072", "#FFFF00", "#BDB76B", "#4169E1", "#696969", "#808000"]
    color = colors[int(male != 1) * 4 + (age % 4)]
    image = "M" * male + "F" * (not male) + "B" * (age >= 21) + "M" * (age < 21)
    print(image, male, int(male != 1) * 4 + (age % 4))
    return render_template("Цвет каюты.html", col=color, img=image)

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1", debug=True)