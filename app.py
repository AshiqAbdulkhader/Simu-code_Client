from flask import Flask, render_template, flash, redirect, Markup, request
from flask.helpers import url_for
from formspages import LoginForm
import requests, json
from validate import auth

RUN_URL = 'http://13.234.251.104:8000/compile/'

app = Flask(__name__)

app.config['SECRET_KEY'] = '908449bd184d0c4d6ee71af64324610e'

@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        uname = request.form['username']
        pwd = request.form['password']
        if auth(uname,pwd):
            flash(f'Logged in as {form.username.data}', 'success')
            return redirect(url_for('index'))
    return render_template('login.html', title='Login', form = form)

@app.route('/index')
def index():
    return render_template('index.html')

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


if __name__ == "__main__":
    app.run()
