# from itertools import permutations

n = 4

# def solution(n):
#     answer = 0
#     for i in range(n,1,-1):
#         if n%i == 0:
#             answer += 1
#         else:
#             answer += i
#         print(answer)
    
#     return answer%1234567

def solution(n):
    dp = [0] * 2001
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % 1234567

print(solution(n))
