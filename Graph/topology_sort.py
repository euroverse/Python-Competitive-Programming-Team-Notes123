from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

''' [ Topology Sort ]
- 위상정렬 : DAG 그래프에서 노드를 순서대로 나열 Ex. 선수 과목
- 진입차수(Indegree) : 노드로 들어오는 간선의 갯수

1. 진입차수가 0인 모든 노드를 큐에 넣는다. (큐에 넣는 순서 == 위상정렬)
2. 큐가 빌 때까지 반복,
   큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
   새롭게 진입차수가 0이 된 노드를 큐에 넣는다
   
(스택과 DFS를 활용한 위상정렬 방법도 있음.)
'''
def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()

'''
[Input Example 1]
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
[Output Example 1]
1 2 5 3 6 4 7
'''
