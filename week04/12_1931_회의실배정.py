import sys
input = sys.stdin.readline

n = int(input())

rooms = [list(map(int, input().rstrip().split())) for _ in range(n)]


rooms = sorted(rooms, key=lambda x:x[0])
rooms = sorted(rooms, key=lambda x:x[1])

end_time = rooms[0][1]

cnt = 1
for i in rooms[1:]:
    start,end = i

    if end_time <= start:
        cnt += 1
        end_time = end
    
print(cnt)

