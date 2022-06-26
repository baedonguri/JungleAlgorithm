name = "JAZ"
# name = "AAAABABAAAA"
# name = "JEROEN"	
def check(alpha):
    move1 = ord(alpha) - ord('A')
    move2 = ord('Z') - ord(alpha)
    return min(move1, move2+1)

# def solution(name):
#     cmp_word = ['A']*len(name)
#     answer = 0 
#     for i in range(len(name)-1):
#         if name[i] == 'A':
#             answer += 1
#         else:
#             answer += check(name[i])
#             cmp_word[i] = name[i]
#             answer += 1
#     if "".join(map(str,cmp_word)) != name: 
#         answer += check(name[-1])
#     return answer


def solution(name):
    min_l_r = len(name)
    answer = 0
    next_idx = 0
    for idx, alpha in enumerate(name):
        answer += check(alpha)

        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
        
        min_l_r = min(min_l_r, idx*2 + len(name)-next_idx)
    answer += min_l_r
    return answer

print(solution(name))



def solution(name):
    answer = 0
    min_left_right = len(name) # 왼쪽에서 오른쪽으로만 이동할 때 좌,우 조작 횟수
    next_idx = 0
    for idx, char in enumerate(name):
        # 위, 아래 조작 횟수의 최솟값 구하기
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 좌, 우 조작 횟수의 최솟값 구하기
        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1 # 현재 위치 이후 연속된 A 다음의 문자를 가리킴
        
        # 한 방향으로만 이동하는 경우와, 오른쪽으로 이동했다가 왼쪽으로 이동하는 경우를 비교
        min_left_right = min(min_left_right, idx + idx + len(name) - next_idx)
    answer += min_left_right
    return answer





# 위로 이동 'A' -> 'J' = 9
# 아래 이동 'A' -> 