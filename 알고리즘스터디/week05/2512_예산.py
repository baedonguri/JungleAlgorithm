# 백준 2512 예산
# 이분 탐색
import sys
input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().split()))
M = int(input())

start,end = 0, max(budgets)
answer = 0

if sum(budgets) < M:
    print(end)
else:
    while start <= end:
        mid = (start + end)//2
        answer = 0
        for budget in budgets:
            answer += min(budget, mid)      
        
        if answer <= M:
            start = mid + 1
        else:
            end = mid - 1
            
    print(end)