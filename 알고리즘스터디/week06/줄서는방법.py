from math import factorial
n, k = 3, 5
def solution(n,k):
    arr = list(range(1,n+1))
    answer  = []
    while n != 0:
        fact = factorial(n-1)
        idx, k = (k-1)//fact, k%fact
        answer.append(arr.pop(idx))
        n -= 1
    return answer

print(solution(n,k))