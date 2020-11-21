from flask import Flask, render_template, request,url_for,Blueprint, flash, redirect
import requests

RUN_URL = 'https://api.hackerearth.com/v3/code/run/'
CLIENT_SECRET = 'e375c29119a4a084d900238b9a3ef841eececd6f'



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    output=None
    code = request.form['code']
    
    data = {
    'client_secret': CLIENT_SECRET,
    'async': 0,
    'source': code,
    'lang': "PYTHON",
    'time_limit': 5,
    'memory_limit': 262144,
    }
    r = requests.post(RUN_URL, data=data)
    print("Output : ",r.json()['run_status']['output_html'])
    return render_template('index.html', output=output)


if __name__ == "__main__":
    app.run()
