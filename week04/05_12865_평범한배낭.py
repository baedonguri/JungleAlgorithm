import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# memorization을 위한 2차원 행렬
P = [[0]*(k+1) for _ in range(n+1)]

wt = []
val = []

for _ in range(n):
    w,v = map(int, input().split())
    wt.append(w)
    val.append(v)

def knapsack():
    # 2차원 행렬의 크기만큼 반복
    for i in range(n+1):
        for w in range(k+1):
            if i == 0 or w == 0:
                P[i][w] = 0
            # 현재 보고 있는 보석을 배낭에 넣을 수 있는 경우
            elif wt[i-1] <= w:
                # 1 : P[i-1][w-wt[i-1] + val[i-1] -> 현재 보석을 넣기 위해 현재 보석만큼의 무게를 비웠을 때의 최적값에 현재 보석값을 더한 결과
                # 2 : P[i-1][w] -> 현재 보석을 제외하고 여태까지 구한 최적값
                # 최적값 중 큰 값을 고름
                P[i][w] = max(P[i-1][w-wt[i-1]]+val[i-1],P[i-1][w])
            else:
                # 넣을 수 없다면 해당 보석을 제외하고 여태까지 구한 최적값을 그대로 가져옴
                P[i][w] = P[i-1][w]
    # 최종 보석 갯수를 출력
    return P[n][k]

print(knapsack())
            