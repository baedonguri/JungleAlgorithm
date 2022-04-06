import sys
input = sys.stdin.readline
a,b = map(str, input().split())
a,b = a[::-1], b[::-1]
print(max(int(a),int(b)))