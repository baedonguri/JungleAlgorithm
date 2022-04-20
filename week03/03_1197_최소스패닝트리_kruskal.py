import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
parent = [i for i in range(v+1)] # 대표 vertex (부모) 저장
graph = []

for _ in range(e):
    a,b,c = map(int, input().split())
    graph.append((c,(a,b)))

# 가중치 기준 오름차순 정렬
graph.sort()
result = 0

# 대표 vertex 반환 / 평탄화 함수
def find(n):
    # 부모를 찾고 자기 자신이면 바로 반환, 자기 자신이 아니면 재귀적 호출 후 대표점 반환

    if parent[n] != n:
        parent[n] = find(parent[n])
        return parent[n]
    return parent[n]
# 합치는 함수
def union(a,b):
    pa = find(a)
    pb = find(b)
    # a와 b의 대표점이 다르면 연결안된 그래프이므로 연결, 같으면 합치지 않음.
    if pa != pb:
        parent[pa] = pb
        return True
    return False

for cost,vertex in graph:
    a, b = vertex
    if union(a,b):
        result += cost
print(result)