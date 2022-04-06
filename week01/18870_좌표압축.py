import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

rank = list(sorted(set(arr)))
# 딕셔너리 인덱싱 사용
# 시간복잡도를 O(1) 시간에 가능
x = {rank[i]:i for i in range(len(rank))}

for i in range(n):
    print(x[arr[i]], end=' ')