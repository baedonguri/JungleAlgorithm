# [프로그래머스] 다음큰숫자 (python)
# https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    MAX_NUM = 1000000
    one_cnt = bin(n).count('1')

    for i in range(n+1, MAX_NUM):
        if one_cnt == bin(i).count('1'):
            return i

print(solution(78))