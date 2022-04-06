import sys
input = sys.stdin.readline

h,w = map(int,input().split())
arr = [list(input().rstrip()) for i in range(h)]

print(arr)