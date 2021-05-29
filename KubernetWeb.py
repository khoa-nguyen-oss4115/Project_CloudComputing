from flask import Flask, render_template, redirect, url_for, request
import os

app = Flask(__name__)

def GetHelmList():
    list = lines = os.popen('helm ls').readlines()
    matrix = []
    for i in list:
        ls = list[i].split('/t')
        matrix.append([0 for c in range(0, len[list[i]])])
    

@app.route("/", methods=["POST", "GET"])
def home():
    GetHelmList()
    if request.method == "POST":
        return render_template("index.html")
    else:
        
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')