def solution(n, lost, reserve):
    set_reserve = list(set(reserve) - set(lost))
    set_lost = list(set(lost) - set(reserve))
    set_reserve.sort()

    for res in set_reserve:
        front, back = res-1, res+1
        if front in set_lost:
            set_lost.remove(front)
        elif back in set_lost:
            set_lost.remove(back)
    return n - len(set_lost)


print(solution(5, [2,4], [1,3,5])) # 5
print(solution(5, [2,4], [3])) # 4
print(solution(3, [3], [1])) # 2