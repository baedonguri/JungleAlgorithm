# [백준] 조합 python
# https://www.acmicpc.net/problem/2407

from math import factorial
from sys import stdin

input = stdin.readline
n,m = map(int ,input().split())

denominator = factorial(n)
numerator = factorial(m) * factorial(n-m)

print(denominator//numerator)

# 조합 공식
# nCr = n! // r! * (n-r)!