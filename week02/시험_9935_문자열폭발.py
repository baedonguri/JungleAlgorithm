import sys
input = sys.stdin.readline

S = input().rstrip()
bomb = input().rstrip()

stack = []

for i in range(len(S)):
    stack.append(S[i])

    if stack and stack[-1] == bomb[-1]:
        temp = stack[len(stack)-len(bomb):]

        if "".join(temp) == bomb:
            for k in range(len(bomb)):
                 stack.pop()

# if stack:
#     print(''.join(stack))
# else:
#     print('FRULA')

print("".join(stack) if stack else "FRULA")