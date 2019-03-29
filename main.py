from flask import Flask,request
app = Flask(__name__)

@app.route("/")
def hello():
    num = float(request.args.get('myVar'))
    print(num)

    res = str(num * 5)
    return res