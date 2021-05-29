import subprocess
#lisy = subprocess.check_output('cmd /k "date"')
#print(lisy)

string = "ng  \tla     \tsa  \n"

sa = string.replace(" ","").split('\t')
sa[len(sa)-1] = sa[len(sa)-1][-2]
print(sa)