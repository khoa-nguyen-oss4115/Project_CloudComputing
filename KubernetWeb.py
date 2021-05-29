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
        if request.form.get("button_c"):
            return render_template("index.html")
        elif request.form.get("button_u"):
            return render_template("index.html")
        elif request.form.get("button_d"):
            return render_template("index.html")
        else:
            return render_template("index.html")
    elif request.method == "GET":
            return render_template("index.html")
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)