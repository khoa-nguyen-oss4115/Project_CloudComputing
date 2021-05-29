from flask import Flask, render_template, redirect, url_for, request
import subprocess
import os

app = Flask(__name__)

def GetHelmList():
    list = os.popen('helm ls').readlines()
    matrix = []
    for i in list:
        ls  = i.replace(" ", "").split('\t')
        ls[len(ls)-1] = ls[len(ls)-1].replace('\n','')
        matrix.append(ls)
    return matrix

@app.route("/", methods=["POST", "GET"])
def home():
    matrix = GetHelmList()
    if request.method == "POST":
        if request.form.get("button_c"):
            return render_template("index.html", list = matrix)
        elif request.form.get("button_u"):
            return render_template("index.html")
        elif request.form.get("button_d"):
            return render_template("index.html")
    elif request.method == "GET":
            return render_template("index.html")
    else:
        return render_template("index.html", list = matrix)

def star_minikube():
    return subprocess.run(["minikube","start"])
def delete_minikube():
    return subprocess.run(["minikube","delete"])
def delete_cluster(name):
    return subprocess.run(["helm","delete",name])
if __name__ == '__main__':
    # print(GetHelmList()[1])
    app.run(debug=True,host='0.0.0.0')