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

def start_minikube():
    subprocess.run(["minikube","start"])

def delete_minikube():
    subprocess.run(["minikube","delete"])

def delete_cluster():
    name = request.form['text']
    subprocess.run(["helm","delete",name])

def create_hadoop():    
    os.system("helm install \
    --set yarn.nodeManager.resources.limits.memory=4096Mi \
    --set yarn.nodeManager.replicas=1 \
    stable/hadoop --generate-name")
def create_redis():
    name = request.form['text']
    subprocess.run(["helm","install",name,"bitnami/redis"])
def create_spark():
    name = request.form['text']
    os.system("helm install %s bitnami/spark" % name)
@app.route("/", methods=["POST", "GET"])
def home():
    matrix = GetHelmList()
    if request.method == "POST":
        if request.form.get("button_start_mini"):
            start_minikube()
            return render_template("index.html", title = matrix[0], list = matrix[1:len(matrix)])
        
        elif request.form.get("button_redis"):
            create_redis()
            matrix= GetHelmList()
            return render_template("index.html", title = matrix[0], list = matrix[1:len(matrix)])
        
        elif request.form.get("button_hadoop"):
            create_hadoop()
            matrix= GetHelmList()
            return render_template("index.html", title = matrix[0], list = matrix[1:len(matrix)])
        elif request.form.get("button_spark"):
            create_spark()
            matrix= GetHelmList()
            return render_template("index.html", title = matrix[0], list = matrix[1:len(matrix)])
        elif request.form.get("button_delete_mini"):
            delete_minikube();
            matrix= GetHelmList()
            return render_template("index.html", title = matrix[0], list = matrix[1:len(matrix)])
    elif request.method == "GET":
        if request.form.get("btn_delete_cluster"):    
            delete_cluster()
            matrix= GetHelmList()
            return render_template("index.html", title = matrix[0], list = matrix[1:len(matrix)])
    else:
        return render_template("index.html", title = matrix[0], list = matrix[1:len(matrix)])

def star_minikube():
    return subprocess.run(["minikube","start"])
def delete_minikube():
    return subprocess.run(["minikube","delete"])

def delete_cluster(name):
    return subprocess.run(["helm","delete",name])
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')