import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

k = int(input())
find = list(map(int, input().split()))
arr.sort()

def search(start, end, key):
    if start > end:
        return 0
    mid = (start+end) // 2
    if arr[mid] == key:
        return 1
    elif arr[mid] > key:
        end = mid - 1
    else:
        start = mid + 1
    
    return search(start, end, key)

for ky in find:
    print(search(0,n-1,ky))