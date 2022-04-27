import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    arr.sort()
    arr = arr[::2]+arr[1::2][::-1]

    ans = 0
    for i in range(n-1):
        ans = max(ans, abs(arr[i+1]-arr[i]))
    print(ans)
