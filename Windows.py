import subprocess
lisy = subprocess.check_output('cmd /k "date"')
print(lisy)