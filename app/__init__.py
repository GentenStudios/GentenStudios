from flask import Flask
from flask import render_template

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")
