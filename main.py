from flask import Flask,request,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/calc")
def hello():
    num = float(request.args.get('myVar'))
    print(num)

    res = str(num * 5)
    return res