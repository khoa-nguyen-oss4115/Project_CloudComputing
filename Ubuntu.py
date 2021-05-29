import subprocess
import os

list = subprocess.run(["helm","ls"])
# print("The exit code was: %d" % list.returncode)
# print(list.stdout)
# output = subprocess.check_output("helm ls", shell=True)
# 
# print(type(output))

# lines = os.popen('helm ls').readlines()
# print(lines[0])

# f= open('file.txt', 'w')
# out = (str)(lines)
# print(out)
# f.write(out)
# f.close()
# print(lines[1])
# text = lines[1].split('\t')
# print(text[0])
# list = lines = os.popen('helm ls').readlines()
# matrix = []
# for i in list:
#     ls  = i.replace(" ", "").split('\t')
#     i[len(i)-1] = i[len(i)-1][-2]
#     matrix.append(ls)
# print(matrix[1][0])
# name = "spark"
# a=  subprocess.run(["helm","delete",name])
# a = os.system("helm install \
#     --set yarn.nodeManager.resources.limits.memory=4096Mi \
#     --set yarn.nodeManager.replicas=1 \
#     stable/hadoop --generate-name")
# b=subprocess.run(["helm install \
#     --set yarn.nodeManager.resources.limits.memory=4096Mi \
#     --set yarn.nodeManager.replicas=1 \
#     stable/hadoop --generate-name"])

# name ="spark"
# os.system("helm install %s bitnami/spark" % name)
os.system("helm install \
    --set yarn.nodeManager.resources.limits.memory=4096Mi \
    --set yarn.nodeManager.replicas=1 \
    stable/hadoop --generate-name")