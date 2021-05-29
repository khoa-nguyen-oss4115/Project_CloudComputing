from flask import Flask, render_template, redirect, url_for, request
import subprocess

app = Flask(__name__)

def Xuly():
    list_files = subprocess.run(["helm ls"])
    print("The exit code was: %d" % list_files.returncode)
    return

@app.route("/", methods=["POST", "GET"])
def home():
    Xuly()
    if request.method == "POST":
        return render_template("index.html")
    else:
        
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')