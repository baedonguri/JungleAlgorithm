# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

# 이동 할 수 있는 최소 거리
start = 1
# 이동 할 수 있는 최대 거리
end = arr[-1] - arr[0]
# 결과값을 저장할 변수
result = 0

while start <= end:
    # 가장 인접한 두 공유기 사이의 거리를 의미
    mid = (start+end)//2
    # 첫번째 집에는 무조건 설치
    var = arr[0]
    cnt = 1
    # 첫번째 집을 제외한 나머지 집을 비교
    for i in range(1,n):
        # 각 집 사이의 거리를 기준으로 설치하는데, 집 사이의 거리보다 짧은 거리는 pass
        # 설치할 경우 설치위치와 다음 집과의 거리를 비교
        if arr[i] >= var + mid:
            var = arr[i]
            cnt += 1
    # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가시키기
    if cnt >= c:
        start = mid + 1
        result = mid
    else: # 설치할 수 없는 경우, 거리를 감소시키기
        end = mid - 1
        
print(result)