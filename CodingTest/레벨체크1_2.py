def solution(s):
    answer = 0
    if s.startswith('-'):
        answer = -int(s[1:])
    return -int(s[1:]) if s.startswith('-') else int(s)