from itertools import combinations
from sys import stdin
input = stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))

maximum = 0
for p in combinations(arr, 3):
    hap = sum(p)
    if hap <= m and maximum < hap:
        maximum = hap

print(maximum)