# -*- coding: utf-8 -*-

import sys
input = sys.stdin.readline

n,r,c = map(int, input().split())
num = 0

while n > 0:
    half = (2**n)//2
    if n > 1:
        if half > r and half <= c:
            num += half**2
            c -= half
        elif half <= r and half > c:
            num += (half ** 2) * 2
            r -= half
        elif half <= r and half <= c:
            num += (half**2)*3
            r -= half
            c -= half
    elif n == 1:
        if r == 0 and c == 1:
            num += 1
        elif r == 1 and c == 0:
            num += 2
        elif r == 1 and c == 1:
            num += 3
        
    n -= 1
    
print(num)
        