import sys
input = sys.stdin.readline


def solution(new_id):
    #1
    new_id = new_id.lower()

    #2
    answer = ''
    for s in new_id:
        if s.isalnum() or s in ['-','_','.']:
            answer += s
    #3
    while '..' in answer:
        answer = answer.replace('..', '.')
    #4
    if answer[0] == '.': 
        if len(answer) >= 2:
            answer = answer[1:]

    if answer[-1] == '.': answer = answer[:-1]

    #5
    if answer == '': answer = 'a'

    #6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    #7
    while len(answer) < 3:
        answer += answer[-1]

    return answer


ans = "=.="
print(solution(ans))
