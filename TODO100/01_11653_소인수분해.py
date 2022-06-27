from sys import stdin
from math import sqrt


input = stdin.readline
n = int(input())
def get_prime(n):
    sieve = [True] * n
    for i in range(2, int(sqrt(n))+1):
        if sieve[i]:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2,n) if sieve[i] == True]

def solution(n):
    primes = get_prime(n)
    if n in primes:
        return n
    answer = []
    i = 0
    while n != 1:
        if n%primes[i] == 0:
            n = n//primes[i]
            answer.append(primes[i])
            continue
        i += 1
    return answer

for i in solution(n):
    print(i)