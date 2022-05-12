from collections import Counter
from sys import stdin

n, m = map(int, input().split())

no_listen = [input().rstrip() for _ in range(n)]
no_see = [input().rstrip() for _ in range(m)]

c_l, c_s = Counter(no_listen), Counter(no_see)

calc = c_l + c_s
answer = [i for i in calc if calc[i] == 2]
answer.sort()
print(len(answer))
print('\n'.join(answer))
