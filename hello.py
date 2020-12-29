from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def hello():
    return render_template('Plastic_collection.html')


@app.route("/sonali")
def sonali():
    return render_template('about.html')


app.run(debug=True)
