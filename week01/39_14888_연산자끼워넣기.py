from itertools import permutations

num = int(input())
arr = list(map(int, input().split()))
cnt_op = list(map(int, input().split()))

op = ['+','-','*','//']
op_ = []

for i in range(4):
    for j in range(cnt_op[i]):
        op_.append(op[i])

perm = list(permutations(op_))
perm = list(set(perm))

answer = []
for p in perm:
    n = arr[0]
    for i in range(num-1):
        if p[i] == '+':
            n += arr[i+1]
        elif p[i] == '-':
            n -= arr[i+1]
        elif p[i] == '*':
            n *= arr[i+1]
        else:
            if n < 0 and arr[i] > 0:
                n = -(-n//arr[i+1])
            else:
                n //= arr[i+1]
    answer.append(n)
    
print(max(answer))
print(min(answer))