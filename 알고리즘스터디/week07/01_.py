# 다시 풀어보기
def solution(k, room_number):
    room_dic = {}
    ret = []
    for i in room_number:
        n = i
        visit = [n]
        while n in room_dic:
            n = room_dic[n]
            visit.append(n)
        ret.append(n)
        for j in visit: room_dic[j] = n + 1
    return ret

k = 10
room_number = [1,3,4,1,3,1]	
print(solution(k,room_number))