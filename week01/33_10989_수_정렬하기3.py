import sys

input = sys.stdin.readline
n = int(input())

check = [0] * 10001

for i in range(n):
    num = int(input())
    check[num] = check[num] + 1
    

for i in range(10001):
    if check[i] != 0:
        for j in range(check[i]):
            print(i)