# def solution(records):
#     answer = []
#     members = {}
#     for record in records:
#         status, id_, *nickname = record.split()
#         if status == 'Enter' or status == 'Change':
#             members[id_] = nickname

#     for record in records:
#         status, id_, *nickname = record.split()

#         user = members[id_][0]
#         if status == 'Enter':
#             answer.append(f'{user}님이 들어왔습니다.')
#         elif status == 'Leave':
#             answer.append(f'{user}님이 나갔습니다.')


#     return answer

def solution(records):
    answer = []
    members = {}
    for record in records:
        status, id_, *nickname = record.split()
        if status in ("Enter", "Change"):
            members[id_] = nickname

    for record in records:
        status, id_, *nickname = record.split()

        user = members[id_][0]
        if status == 'Enter':
            answer.append(f'{user}님이 들어왔습니다.')
        elif status == 'Leave':
            answer.append(f'{user}님이 나갔습니다.')


    return answer
