def solution(s):
    arr = ['000','111','222','333','444','555','666','777','888','999']
    answer = []
    for i in arr:
        if i in s:
            answer.append(int(i))
    
    return max(answer) if answer else -1
