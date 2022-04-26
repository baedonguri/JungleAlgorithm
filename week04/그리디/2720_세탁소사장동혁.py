import sys
input = sys.stdin.readline

coins = [25,10,5,1]

for _ in range(int(input())):
    c = int(input())
    table = []

    for coin in coins:
        table.append(c//coin)
        c %= coin
        
    print(*table)

    