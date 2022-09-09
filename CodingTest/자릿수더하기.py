def solution(n):
    import re
    arr = re.findall(r'\d', str(n))
    return sum(map(int, arr))