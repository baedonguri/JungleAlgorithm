import sys
input = sys.stdin.readline
n = int(input())
arr = [input().split() for _ in range(n)]

arr.sort(key=lambda x: int(x[0]))

for i in arr:
    print(*i)