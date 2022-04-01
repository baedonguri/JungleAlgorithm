import sys
a,b,v = map(int,sys.stdin.readline().split())

dist = 0
day = 0

while True:
    dist += a
    day += 1
    if dist >= v:
        break
    dist -= b
    
print(day)