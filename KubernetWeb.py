from flask import Flask, render_template, redirect, url_for, request
import os

app = Flask(__name__)

def GetHelmList():
    list = os.popen('helm ls').readlines()
    matrix = []
    for i in list:
        ls  = i.replace(" ", "").split('\t')
        ls[len(ls)-1] = ls[len(ls)-1][-2]
        matrix.append(ls)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        return render_template("index.html")
    else:
        if request.method == "GET":
            return render_template("index.html")
        else:


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')