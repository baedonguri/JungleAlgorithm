from collections import Counter
import sys
input = sys.stdin.readline

def solution(lottos, win_nums):
    answer = [0,0]
    check = 0
    for lotto in lottos:
        if lotto in win_nums:
            check += 1

    min_rank = check
    max_rank = check + lottos.count(0)

    answer[0] = check_rank(max_rank)
    answer[1] = check_rank(min_rank)

    return answer

def check_rank(num):
    if num <= 1: return 6
    elif num == 2: return 5
    elif num == 3: return 4
    elif num == 4: return 3
    elif num == 5: return 2
    else: return 1

lottos = [45, 4, 35, 20, 3, 9]	
win_nums = [20, 9, 3, 45, 4, 35]	

print(solution(lottos, win_nums))