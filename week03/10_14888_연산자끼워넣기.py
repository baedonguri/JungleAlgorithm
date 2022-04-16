import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))


cnt = [-1e9,1e9] # maximum, minimum

def dfs(depth, total, plus, minus, mul, div):
    if depth == n:
        cnt[0] = max(total, cnt[0])
        cnt[1] = min(total, cnt[1])
        return

    if plus:
        dfs(depth+1, total+nums[depth], plus-1, minus, mul, div)    
    if minus:
        dfs(depth+1, total-nums[depth], plus, minus-1, mul, div)    
    if mul:
        dfs(depth+1, total*nums[depth], plus, minus, mul-1, div)
    if div:
        dfs(depth+1, int(total/nums[depth]), plus, minus, mul, div-1)


dfs(1, nums[0], op[0],op[1], op[2], op[3])
print(cnt[0])
print(cnt[1])