# 프로그래머스 가장큰수
# https://programmers.co.kr/learn/courses/30/lessons/42746#
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x : x*3, reverse=True)
    # 333, 303030, 343434, 555, 999
    return str(int("".join(numbers)))
        
    
numbers = [3, 30, 34, 5, 9]
print(solution(numbers))
