import random

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world!"

@app.route('/<name>')
def rand(name):
    num = random.randint(0,999)
    return render_template('rand.html', name=name, num=num)

app.run(host='0.0.0.0')
