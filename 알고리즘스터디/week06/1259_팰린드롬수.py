from collections import deque
from sys import stdin
input = stdin.readline
def check(string):
    que = deque(string)
    while que:
        front = que.popleft()
        if que:
            back = que.pop()
            if front == back:
                continue
            else:
                return "no"
        else:
            break
    return "yes"


while True:
    num = input().rstrip()
    if num == "0": break
    answer = check(num)
    print(answer)

