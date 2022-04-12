import sys
input = sys.stdin.readline

N,K = map(int, input().split())
num = list(input())

stack = []
cnt = 0

for i in range(N):
    while cnt < K and stack and stack[-1] < num[i]:
        stack.pop()
        cnt += 1
    stack.append(num[i])

    
# print(''.join(stack))
for i in range(N-K):
    print(stack[i],end='')