from sys import stdin
input = stdin.readline
n = int(input())

for i in range(1,n+1):
    tmp = i + sum(map(int, list(str(i))))
    if tmp == n:
        print(i)
        break
else:
    print(0)

