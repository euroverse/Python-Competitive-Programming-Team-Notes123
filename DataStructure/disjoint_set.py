''' [ Disjoint Set ]
- 서로소 집합은 공통 원소가 없는 두 집합을 의미한다.
- 서로소 집합 자료구조는 Union과 Find 연산을 수행한다.
- Union : 두 원소가 포함된 집합을 하나로 합치는 연산
- Find  : 해당 원소가 속한 집합의 루트 노드를 반환
'''

# Find the root node of x recursively.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# Union the two sets.
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

# Process union operations.
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('Root nodes for all nodes: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

print('Parent Table: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')

'''
[Input Example 1]
6 4
1 4
2 3
2 4
5 6
[Output Example 1]
Root nodes for all nodes: 1 1 1 1 5 5 
Parent Table: 1 1 1 1 5 5
'''

''' [ Find Cycle ]
- 서로소 집합 자료구조는 무방향 그래프의 사이클 판별에 사용된다.
- 모든 간선을 하나씩 확인,
  양 끝 노드가 같은 집합이면 => 사이클 존재
  양 끝 노드가 다른 집합이면 => Union 수행
'''
cycle = False
for i in range(e):
    a, b = map(int, input().split())
    
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    
    else: union_parent(parent, a, b)
print(cycle)