import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
dist = min(arr)

for i in range(2):
    if arr[i+2]-arr[i] < dist:
        dist = arr[i+2]-arr[i]
print(dist)