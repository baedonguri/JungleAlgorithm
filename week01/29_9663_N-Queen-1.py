import sys

input = sys.stdin.readline

N = int(input())
cnt = 0
row = [0]*N
visit = [False] * N

def check(Q):
    for i in range(Q):
        if abs(row[Q] - row[i]) == Q-i:
            return False
    return True


def dfs(Q):
    global cnt
    if Q == N:
        cnt += 1
        return
    
    for i in range(N):
        if visit[i]:
            continue
            
        row[Q] = i
        if check(Q):
            visit[i] = True
            dfs(Q+1)
            visit[i] = False
dfs(0)
print(cnt)