from sys import stdin
input = stdin.readline
n,m = map(int, input().split())
videos = list(map(int,input().rstrip().split()))
start = max(videos)
end = sum(videos)

while start <= end:
    mid = (start+end)//2
    cnt = 1
    total = 0
    for i in range(n):
        if total + videos[i] <= mid:
            total += videos[i]
        else:
            cnt += 1
            total = videos[i]
    