
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    name= "Frnce"
    current_year="2070"

    cities = ["Prnjavor", "Maribor", "Titograd"]
    #return "Hello, SmartNinja!"
    return render_template("index.html", name=name, current_year=current_year,
                           cities=cities)

@app.route("/about")
def about_me():
    #return "Hello, SmartNinja!"
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    #return "Hello, SmartNinja!"
    return render_template("portfolio.html")

@app.route("/contacts")
def contacts():
    #return "Hello, SmartNinja!"
    return render_template("contacts.html")



if __name__ == '__main__':
    app.run()