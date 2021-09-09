from flask import Flask, render_template, request
from getBusInfo import getBusInfo

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/busInfo")
def busInfo():
    atcocode = request.args.get('atcocode')
    busInfo = getBusInfo(atcocode)
    return render_template('info.html', atcocode=atcocode, items=busInfo)

if __name__ == "__main__": app.run()