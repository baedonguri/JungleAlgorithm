import sys
from collections import defaultdict
input = sys.stdin.readline

n,m = map(int, input().split())

# 1단계 : 정방향 인접 리스트와 역방향 인접 리스트를 각각 생성
adj_f = defaultdict(list) # forward
adj_b = defaultdict(list) # backward

for _ in range(m):
    v1, v2 = map(int, input().split())
    adj_f[v1].append(v2)
    adj_b[v2].append(v1)

# 2단계 : DFS 함수 생성
def dfs(adj, v1, parent, results):
    if v1 in adj:
        for v2 in adj[v1]:
            if v2 not in parent:
                parent[v2] = v1
                dfs(adj, v2, parent, results)
    results.append(v1)

# 3단계 : 각 정점을 시작점으로 DFS를 실행했을 때, 해당 정점의 자손 개수를 카운트
answers = set()
for v1 in range(1, n+1):
    # 정방향 그래프 탐색 (오름차순)
    parent, results = {},[]
    parent[v1] = 0
    print(f'v1:{v1},result : {results}')
    dfs(adj_f, v1, parent, results)
    # 본인을 제외한 자손들의 수 확인
    # - 본인 제외 자손들의 수가 (n+1)//2 이상이면 본인은 가운데에 올 수 없음
    # - 구슬이 5개 일 때, 자손이 3개 이상이면 본인의 인덱스는 중간인 2보다 커짐
    print(f'v1:{v1},result : {results}')
    print()

    if len(results)-1 >= (n+1)//2:
        answers.add(v1)
        continue
    # 역방향 그래프 탐색 (내림차순)
    parent, results = {},[]
    parent[v1] = 0
    dfs(adj_b, v1, parent, results)

    if len(results)-1 >= (n+1)//2:
        answers.add(v1)

print(len(answers))
print(answers)