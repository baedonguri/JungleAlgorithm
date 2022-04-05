import sys
input = sys.stdin.readline

cnt = 0

def check(r,c,half):
    if half > r and half <= c:
        return 2
    elif half <= r and half > c:
        return 3
    elif half <= r and half <= c:
        return 4
    else:
        return 1

def recursive(n,r,c):
    global cnt
    
    half = (2**n)//2
    loc = check(r,c,half)
        
    if n > 1:
        if loc == 2:
            cnt += half**2
            recursive(n-1, r,c-half)
        elif loc == 3:
            cnt += (half**2)*2
            recursive(n-1, r-half,c)
        elif loc == 4:
            cnt += (half**2)*3
            recursive(n-1, r-half,c-half)
        else:
            recursive(n-1,r,c)
    else:
        if r == 0 and c == 1:
            cnt += 1
        elif r == 1 and c == 0:
            cnt += 2
        elif r == 1 and c == 1:
            cnt += 3
            
n,r,c = map(int, input().split())
recursive(n,r,c)

print(cnt)