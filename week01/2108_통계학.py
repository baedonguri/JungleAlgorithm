from collections import Counter
import sys
input = sys.stdin.readline

arr = []
n = int(input())
arr = [int(input()) for i in range(n)]
arr.sort()

print(int(round(sum(arr)/n)))
print(arr[n//2])
cnt = Counter(arr).most_common(2)

if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
    
print(abs(min(arr)-max(arr)))