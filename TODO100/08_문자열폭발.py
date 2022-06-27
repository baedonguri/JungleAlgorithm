from sys import stdin
input = stdin.readline

string = input().rstrip()
bomb = input().rstrip()
stack = []
for s in string:
    stack.append(s)
    if stack and stack[-1] == bomb[-1]:
        tmp = stack[-len(bomb):]
        if "".join(tmp) == bomb:
            del stack[-len(bomb):]

print("".join(stack) if stack else 'FRULA')

