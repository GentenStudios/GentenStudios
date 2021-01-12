from flask import Flask, session, redirect, url_for, request, render_template
from markupsafe import escape

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.debug = True


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'
    # return render_template("about.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
