import re

info = ["java backend junior pizza 150",
"python frontend senior chicken 210",
"python frontend senior chicken 150",
"cpp backend senior pizza 260",
"java backend junior chicken 80",
"python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
"python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250",
"- and backend and senior and - 150",
"- and - and - and chicken 100",
"- and - and - and - 150"]

info_data = []
query_data = []
for i in info:
    info_data.append(i.split(" "))

for i in info_data:
    print(i)


