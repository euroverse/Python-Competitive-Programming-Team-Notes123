from collections import deque

''' Breadth First Search (BFS) with Queue
스택 또는 재귀함수로 구현하는 DFS와 달리,
BFS는 큐 자료구조를 이용해 구현한다. (큐는 덱 라이브러리로 구현)

1. BFS는 해당 시점의 인접 노드를 모두 큐에 넣는 것이 특징적이다.
2. BFS는 최단 경로와 최단 거리 문제에 자주 이용된다.

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼내어 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리.
3. 2번 반복

★ 최단 경로 알고리즘 BFS VS Dijkstra
BFS: 가중치가 없는 그래프(=정점 사이의 거리가 모두 같을 때) 사용.
Dijkstra: 가중치가 있는 그래프에서 사용. 더 빨리 갈 수 있는 길을 새롭게 찾아내는 과정을 거침.

두 알고리즘 모두 "한 정점으로부터 모든 정점까지의 최단거리"를 구할 수 있음.
단 BFS의 경우 1.배열을 이용해 모든 최단거리 저장할지 2.큐에 거리를 저장해서 도착 정점까지의 최단거리만 구할지로 나뉨.

'''
def bfs(x):
    q = deque([x])
    visited[x] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for y in graph[x]:
            if not visited[y]:
                q.append(y)
                visited[y] = True 
'''
큐에 넣어줄 때 방문여부를 확정하자(=최단거리를 확정한다)
=> BFS라서 처음 넣어줄 때 확정지어도 상관 없음.
=> 무엇보다, 한 번 넣었던게 다시 큐에 들어가는 일을 방지해줌.

큐에서 꺼낼 때 방문여부를 확정하면 여러가지 변수가 생김.
'''
                
n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for e in graph:
    e.sort()

visited = [False] * (n + 1)
bfs(start)

'''
[Input Example 1]
4 5 1
1 2
1 3
1 4
2 4
3 4
[Output Example 1]
1 2 3 4
'''