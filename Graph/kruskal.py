''' [ Kruskal Algorithm]
- 대표적인 최소 신장 트리 알고리즘
- 그래프 내의 모든 정점들을 최소 비용으로 연결하기 위해 사용
- 사이클 발생여부 확인을 위해 서로소 집합 자료구조를 활용한다.

1. 간선을 비용에 따라 오름차순 정렬
2. 간선을 하나씩 확인하며,
   사이클 발생O => 최소신장트리에 포함X
   사이클 발생X => 최소신장트리에 포함O
'''

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else: parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)
edges = []
result = 0

for i in range(1, v+1): parent[i] = i

for _ in range(e):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))

edges.sort()

for w, a, b in edges:
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    else:
        union_parent(parent, a, b)
        result += w

print(result)