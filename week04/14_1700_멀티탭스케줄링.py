import sys
input = sys.stdin.readline

n, k = map(int, input().split())
taps = list(map(int, input().split()))
cur_tap = []
cnt = 0
for i in range(k):
    if taps[i] in cur_tap:
        continue
    if len(cur_tap) < n:
        cur_tap.append(taps[i])
        continue

    idxs = []
    for j in range(n):
        try:
            idx = taps[i:].index(cur_tap[j])
        except:
            idx = 101
        idxs.append(idx)

    tap_out = idxs.index(max(idxs))
    del cur_tap[tap_out]
    cur_tap.append(taps[i])
    cnt += 1
    
print(cnt)