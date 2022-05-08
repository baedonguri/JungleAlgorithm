def solution(atmos):
    answer = 0
    cnt = 0
    for atmo in atmos:
        mise, c_mise = atmo        
        if not cnt:
            if mise > 150 and c_mise > 75:
                answer += 1
                cnt = 0
            elif mise > 80 or c_mise > 35:
                answer += 1
                cnt += 1
        else:
            if mise > 150 and c_mise > 75: cnt = 0
            else: cnt += 1

        if cnt == 3: cnt = 0

