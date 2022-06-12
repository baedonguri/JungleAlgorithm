from sys import stdin
input = stdin.readline
num = int(input())
string = input().rstrip()
answer = 0
for i,a in enumerate(string):
    answer += (ord(a)-96) * 31**i 

print(answer%1234567891)