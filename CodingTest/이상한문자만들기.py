def convert(s):
    result = ''
    for idx,w in enumerate(s):
        if idx%2: result += w.lower()
        else:  result += w.upper()
    return result

def solution(s):
    arr = [convert(i) for i in s.split(' ')]
    return " ".join(arr)


print(solution("try hello world"))