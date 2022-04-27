import sys
input = sys.stdin.readline

n = int(input())

rope = [int(input()) for _ in range(n)]
rope.sort()

result = []
cnt = 0
for i in rope:
    result.append(i*n)
    n -= 1

print(max(result))
