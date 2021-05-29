import subprocess
#lisy = subprocess.check_output('cmd /k "date"')
#print(lisy)

list = ['NAME             \tNAMESPACE\tREVISION\tUPDATED                                \tSTATUS  \tCHART       \tAPP VERSION\n', 'hadoop-1622222000\tdefault  \t1       \t2021-05-28 10:13:25.304443512 -0700 PDT\tdeployed\thadoop-1.1.4\t2.9.0      \n', 'hung-redis       \tdefault  \t1       \t2021-05-28 10:12:42.394263199 -0700 PDT\tdeployed\tredis-14.3.2\t6.2.3      \n', 'spark            \tdefault  \t1       \t2021-05-28 10:17:53.215173698 -0700 PDT\tdeployed\tspark-5.4.3 \t3.1.1      \n']
matrix = []
for i in list:
    ls  = i.replace(" ", "").split('\t')
    ls[len(ls)-1] = ls[len(ls)-1].replace('\n','')
    matrix.append(ls)

print(matrix)