def is_prime(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    for i in range(2, n):
        if n%i == 0:
            return 0
    return 1

n = int(input())
arr = list(map(int, input().split()))
cnt = 0

for i in arr:
    if is_prime(i):
        cnt += 1
        
print(cnt)