a = int(input())
b = int(input())
c = int(input())

s_list = str(a*b*c)

for i in range(10):
    print(s_list.count(str(i)))