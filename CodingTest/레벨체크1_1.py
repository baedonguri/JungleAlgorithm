def solution(n):
    answer = [False, False] + [True] * (n-1)
    primes = []

    for i in range(2, n+1):
        if answer[i]:
            primes.append(i)
            for j in range(2*i,n+1,i):
                answer[j] = False

    return len(primes)