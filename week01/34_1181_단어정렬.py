import sys
input = sys.stdin.readline

n = int(input().strip())

word = [input().rstrip() for i in range(n)]
word = list(set(word))

word = sorted(word)

word = sorted(word, key=lambda x:len(x))

for i in word:
    print(i)