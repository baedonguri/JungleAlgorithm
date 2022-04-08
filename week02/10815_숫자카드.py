import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))
arr.sort()

def search(key):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == key:
            return 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in find:
    print(search(i),end=' ')