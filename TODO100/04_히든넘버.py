import re
from sys import stdin
input = stdin.readline

n = int(input())
words = input().rstrip()
numbers = re.findall(r'\d+', words)
print(sum([int(num) for num in numbers]))