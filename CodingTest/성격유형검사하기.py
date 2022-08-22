from collections import defaultdict
def solution(survey, choices):
    answer = ''
    dic = {
        'R' : 0, 'T' : 0,
        'C' : 0, 'F' : 0,
        'J' : 0, 'M' : 0,
        'A' : 0, 'N' : 0   
    }
    score_chart = {1:3, 2:2, 3:1, 5:1,6:2,7:3}
    for sur, score in zip(survey, choices):
        x,y = sur
        if score in [1,2,3]:
            dic[x] += score_chart[score]
        elif score in [5,6,7]:
            dic[y] += score_chart[score]
        else:
            continue
    template = [['R','T'],['C','F'],['J','M'],['A','N']]
    for i in range(4):
        l,r = template[i]
        winner = r if dic[l] < dic[r] else l
        answer += winner
        
    return answer