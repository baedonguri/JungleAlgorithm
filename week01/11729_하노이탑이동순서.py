import sys
input = sys.stdin.readline

def hanoi(n, from_,mid_,to_):
    if n==1:
        print(from_,to_)
        return
    
    hanoi(n-1, from_,to_,mid_)
    print(from_,to_)
    hanoi(n-1, mid_,from_,to_)

n = int(input())
move = 2**n-1
print(move)
hanoi(n,1,2,3)