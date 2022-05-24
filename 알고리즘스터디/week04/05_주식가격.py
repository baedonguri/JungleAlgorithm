# 프로그래머스 - 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

from collections import deque

def solution(prices):
    que = deque(prices) 
    result = []

    while que:
        cnt = 0
        q = que.popleft()

        for i in que[]:
            cnt += 1
            if q > i: break
        result.append(cnt)

    return result

print(solution([1, 2, 3, 2, 3]))