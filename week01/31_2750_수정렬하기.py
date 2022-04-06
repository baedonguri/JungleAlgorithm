import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for i in range(n)]
arr = sorted(arr)
for i in arr:
    print(i)