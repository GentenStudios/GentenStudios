from flask import Flask, session, redirect, url_for, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
from .models import User


def init(app: Flask, db: SQLAlchemy):

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
        # remove the username from the session if it's there
        session.pop('username', None)
        return redirect(url_for('index'))
