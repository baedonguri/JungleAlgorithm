# def solution(W,H):
#     import math
#     W, H = 8, 12
#     c = (W**2) + (H**2) 
#     total = W*H
#     result = total - math.ceil(math.sqrt(c))-1

#     return result


# print(solution(8,12))

def gcd(a,b):
    tmp = a%b
    while tmp != 0:
        a = b
        b = tmp
        tmp = a%b
    return abs(b)


def solution(W,H):
    area = W*H
    check = W + H - gcd(W,H)
                       
    return area-check
    

print(solution(8,12))


