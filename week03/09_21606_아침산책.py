import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(v):
    cnt = 0
    for n in edge[v]:
        # 인접한 곳이 실내라면 카운트
        if A[n] == 1:
            cnt += 1
        else:
            # 실외일 경우 dfs로 주변의 인접 실내를 카운트
            if n not in check:
                check.add(n)
                cnt += dfs(n)
    return cnt


N = int(input())

A = [0] + list(map(int,input().rstrip()))

edge = [[] for _ in range(N+1)]

for _ in range(1,N):
    x,y = map(int, input().split())
    edge[x].append(y)
    edge[y].append(x)


count = 0
check = set()

for i in range(1, N+1):
    # 각 실내별 인접한 실내 구하기
    if A[i] == 1:
        for j in edge[i]:
            if A[j] == 1:
                count += 1
    # 인접한 실외를 한 컴포넌트로 보고, 그 컴포넌트에 인접한 실내의 수를 구한 뒤
    # 각 컴포넌트별로 n*(n-1)의 경우의 수를 계산
    else: 
        if i not in check:
            check.add(i)
            tmp = dfs(i)
            count += tmp * (tmp-1)

print(count)