from flask import Flask, render_template, request, Markup
import requests, json

RUN_URL = 'http://7e82e892235e.ngrok.io/compile/'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    lang = str(request.form.get('lang'))
    code = request.form['code']
    print(lang)
    data = {
        "source":code,
        "lang":lang,
        "id":1,
    }
    
    data=json.dumps(data)
    r = requests.post(RUN_URL, data=data)
    output = Markup(json.loads(r.json())["msg"])
    return render_template('index.html', output=output, code=code, lang=lang)


if __name__ == "__main__":
    app.run()
