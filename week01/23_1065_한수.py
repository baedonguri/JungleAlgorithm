import sys

input = sys.stdin.readline

n = int(input())

cnt = 0

if n < 100:
    cnt = n

else:
    cnt = 99
    for i in range(100, n+1):
        th = i//100
        hu = i%100//10
        te = i%100%10
        if (hu-th) == (te-hu):
            cnt += 1
        
print(cnt)
    