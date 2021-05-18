from flask import Flask, render_template, flash, redirect, Markup, request, session
from flask.helpers import get_flashed_messages, url_for
from formspages import LoginForm
import requests, json
from validate import auth

RUN_URL = 'http://35.154.94.183:8000/compile/'

app = Flask(__name__)

app.config['SECRET_KEY'] = '908449bd184d0c4d6ee71af64324610e'

@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        uname = request.form['username']
        pwd = request.form['password']
        if auth(uname,pwd):
            if 'uid' in session and session['uid'] == uname:
                return redirect(url_for('index')) #Need to handle this better
            else:
                session['uid'] = uname
                return redirect(url_for('index'))
    return render_template('login.html', title='Login', form = form)

@app.route('/index')
def index():
    if 'uid' in session:
        uname = session['uid']
    return render_template('index.html', uname = uname)

@app.route('/index', methods=['POST'])
def getvalue():
    lang = str(request.form.get('lang'))
    code = request.form['code']
    theme = str(request.form['theme'])
    data = {
        "source":code,
        "lang":lang,
        "id":1,
    }
    data=json.dumps(data)
    r = requests.post(RUN_URL, data=data)
    output = Markup(json.loads(r.json())["msg"])
    return render_template('index.html', output=output, code=code, lang=lang, theme=theme)

@app.route('/logout')
def logout():
    session.pop('uid', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run()
