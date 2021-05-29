import subprocess

list = subprocess.run(["helm ls"])
print("The exit code was: %d" % list.returncode)