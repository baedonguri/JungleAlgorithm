from sys import stdin
input = stdin.readline
x = input().rstrip()

answer = 0
if x.startswith('0x'):
    s_len = len(x[2:])-1
    for i in x[2:]:
        answer += int(i,16) * (16 ** s_len)
        s_len -= 1
elif x.startswith('0'):
    s_len = len(x[1:])-1
    for i in x[1:]:
        answer += int(i,8) * (8 ** s_len)
        s_len -= 1
else:
    answer = int(x)

print(answer)