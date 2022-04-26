import sys
input = sys.stdin.readline

N,T = map(int, input().split())

times = []
scores = []

for _ in range(N):
    k, s = map(int, input().split())
    times.append(k)
    scores.append(s)

P = [[0]*(T+1) for _ in range(N+1)]

for i in range(N+1):
    for t in range(T+1):
        if i == 0 or t == 0:
            P[i][t] = 0
        
        elif times[i-1] <= t:
            P[i][t] = max(P[i-1][t-times[i-1]]+scores[i-1], P[i-1][t])
        else:
            P[i][t] = P[i-1][t]
    
print(P[N][T])

                
