from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world!"

visits = 0
@app.route('/<name>')
def visit(name):
    global visits
    visits += 1
    return render_template('visit.html', name=name,
                           visits=visits)

app.run(host='0.0.0.0')
