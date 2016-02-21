from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:////root/app.db'

db = SQLAlchemy(app)

class Page(db.Model):
    name = db.Column(db.Text(), primary_key=True)
    visits = db.Column(db.Integer)

db.drop_all()
db.create_all()

@app.route('/<name>')
def visit(name):
    p = db.session.query(Page).get(name)
    if not p:
        p = Page(name=name, visits=0)
        db.session.add(p)
        db.session.flush()
    p.visits += 1
    db.session.commit()
    return render_template('visit.html', name=name, visits=p.visits)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
