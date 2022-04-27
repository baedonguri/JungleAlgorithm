import sys
input = sys.stdin.readline

t = int(input())
btn = [300,60,10]

ans = []
for b in btn:
    ans.append(t//b)
    t %= b
    
if t == 0: print(*ans)
else: print(-1)