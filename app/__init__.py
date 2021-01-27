import os

from flask import Flask, session, redirect, url_for, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape

app = Flask(__name__, instance_relative_config=True)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app.models import User
from app.models import Module


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/users')
def users():
    try:
        _users = User.query.all()
        return jsonify([e.serialize() for e in _users])
    except Exception as e:
        return str(e)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        _username = request.form['username']
        _match = User.query.filter_by(username=_username).first()
        if _match is None:
            return redirect(url_for("login", error="Username not found"))
        session['username'] = _username
        return redirect(url_for("index"))
    _error = request.args.get('error')
    return render_template("login.html", error=_error)


@app.route('/users/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        try:
            user = User(
                username=username,
                email=email
            )
            db.session.add(user)
            db.session.commit()
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        except Exception as e:
            return str(e)
    return render_template("register.html")


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/marketplace')
def marketplace():
    try:
        _modules = Module.query.all()
        return render_template("marketplace.html", modules=_modules)
    except Exception as e:
        return str(e)


@app.route('/marketplace/new', methods=['GET', 'POST'])
def add_module():
    if request.method == 'POST':
        if not session['username']:
            return redirect(url_for('login'))
        name = request.form['name']
        source = request.form['source']
        try:
            user = User.query.filter_by(username=session['username']).first()
            print(user.modules)
            user.modules += [Module(
                name=name,
                source=source
            )]
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('marketplace'))
        except Exception as e:
            return str(e)
    return render_template("add_module.html")


@app.route('/marketplace/<module_id>')
def module(module_id):
    try:
        _module = Module.query.filter_by(id=module_id).first()
        return render_template("module.html", module=_module)
    except Exception as e:
        return str(e)
