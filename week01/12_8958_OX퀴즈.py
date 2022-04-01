def solution(string):
    score = 0
    cnt = 0
    for i in string:
        if i == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0

    return score


num = int(input())

for i in range(num):
    case = input()
    print(solution(case))