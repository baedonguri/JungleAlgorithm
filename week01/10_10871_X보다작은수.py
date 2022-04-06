import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

arr = [i for i in arr if i < x]

# print(*arr)
print(arr)