from sys import stdin
input = stdin.readline
MAX_NUM = 123456
def getPrimes():
    primes = [False,False] + [True] * (MAX_NUM*2-1)
    result = []  
    for i in range(2,(MAX_NUM*2)+1):
        if primes[i]:
            result.append(i)
        for j in range(2*i,(MAX_NUM*2)+1, i):
            primes[j] = False         
    return result

primes = getPrimes()

while True:
    n = int(input().rstrip())
    cnt = 0
    if n == 0: break
    for i in primes:
        if i > 2*n: break
        if n < i:
            cnt += 1
    print(cnt)