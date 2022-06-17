from heapq import heapify, heappush, heappop
import re
from time import time
n = 2
t = 10
m = 2
# timetable = ["08:00", "08:01", "08:02", "08:03"]	
timetable = ["09:10", "09:09", "08:00"]	
# 09:00부터 총 n회 t분 간격으로 역에 도착
# 하나의 셔틀에는 최대 m명 탑승
# 셔틀 도착시, 대기열에 선 크루를 대기 순서대로 태운 뒤, 바로 출발

# timetable = sorted(table, key=lambda x : (x[0], x[1]))
# def compare(time1, time2):
#     h_1 = int(time1[0])
#     h_2 = int(time2[0])
#     m_1 = int(time1[1])
#     m_2 = int(time2[1])
#     if h_1 >= h_2 or m_1 >= m_2 :
#         return True
#     return False

# max_cnt = 0
# for i in range(len(timetable)):
#     cnt = 0
#     target = timetable[i]
#     for j in range(i, len(timetable)):
#         if compare(target, timetable[j]):
#             print('탑승')
#         else:
#             break


def trans_timetable(timetable):
    table = []
    for time in timetable:
        h,m = time.split(':')
        table.append(int(h)*60+int(m))
    return table

def solution(n,t,m,timetable): 
    timetable = sorted(trans_timetable(timetable))
    busTime = [9*60+t*i for i in range(n)]
    idx = 0
    for i in busTime:
        cnt = 0
        while cnt < m and idx < len(timetable) and timetable[idx] <= i:
            idx += 1
            cnt += 1
        if cnt < m:
            answer = i
        else:
            answer = timetable[idx-1]-1

    return str(answer//60).zfill(2)+":"+str(answer%60).zfill(2)

print(solution(n,m,t,timetable))