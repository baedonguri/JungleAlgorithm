from itertools import product


def solution(word):
    answer = 0
    words = list(word)
    result = []
    for i in range(1,6):
        tmp = product(['A','E','I','O','U'], repeat=i)
        result.extend(list(map("".join, tmp)))
        
    result.sort()
    
    return result.index(word)+1
