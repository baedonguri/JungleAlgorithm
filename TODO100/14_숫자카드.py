from sys import stdin
input = stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
have = list(map(int, input().split()))
cards.sort()

def binary(num):
    start = 0
    end = len(cards)-1
    while start <= end:
        mid = (start+end)//2

        if cards[mid] == num:
            return 1
        elif cards[mid] < num:
            start = mid+1
        else:
            end = mid -1
    return 0


for i in have:
    print(binary(i),end = ' ')