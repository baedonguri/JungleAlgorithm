import math 
def solution(levels):
    min_x, max_x = min(levels), max(levels)

    per = math.ceil((min_x + max_x) * 0.75)

    idx = levels.index(per)

    arr = [level for level in levels[idx:]]

    return min(arr) if arr else -1