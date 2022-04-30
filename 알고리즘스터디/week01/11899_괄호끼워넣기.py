import sys
input = sys.stdin.readline

s = input().rstrip()

length = len(s)

while True:
    s = s.replace("()","")
    length -= 1
    if length == 0:
        print(len(s))
        break

    