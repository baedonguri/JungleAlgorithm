import sys
input = sys.stdin.readline
INF = float("inf")
n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]



def dfs(x, visited):
    if visited == (1<<n) - 1:
        