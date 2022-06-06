arr = list(range(1,11))
num = 6

def solution(n):
    if n <= 3:
        return '124'[n-1]
    else:
        q,r = divmod(n-1,3)
        return solution(q) + '124'[r]

    
# def solution(n):
#     if n <= 3:
#         return '124'[n-1]
#     else:
#         x,y = divmod(n-1, 3)
#         return solution(x) + '124'[y]

print(solution(num))

# 1 0   
# 2 0
# 3 1
# 몫 1이하, 나머지가 0이 아닐 경우

# 4 7   3
# 5 7   2
# 6 8   2
# 몫 2이하, 나머지가 0이 아닐 경우

# 7 21 14  7
# 8 22 14  6
# 9 24 15  6
# 몫 3 이하 
# 10 31

