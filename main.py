from flask import Flask,render_template
import csv


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route("/<name>")
def home(name):
    return render_template('home.html', content=name)
if __name__ == "__main__":
    app.run(debug=True)