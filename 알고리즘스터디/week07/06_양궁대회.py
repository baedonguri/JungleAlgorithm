from itertools import combinations_with_replacement as H

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]	


def compare(a,b):
    return a[::-1] > b[::-1]

def solution(n, info):
    # 라이언이 가장 큰 점수 차이로 우승할 수 있는 결과를 저장
    # ret[0..10] : 10-i점에서 라이언이 맞힌 화살의 수, ret[11] : 점수 차이
    ret = [-1] * 12 
    for comb in H(range(11), n):
        arrow = [0] * 12
        score = 0
        for x in comb: arrow[x] += 1
        for i in range(11):
            if arrow[i] > info[i]:
                score += (10 - i)
            elif info[i] != 0:
                score -= (10 - i)
        if score <= 0: continue
        arrow[11] = score
        if compare(arrow, ret):
            ret = arrow[:] 
    if ret[0] == -1: return [-1]
    return ret[:-1]

print(solution(n,info))