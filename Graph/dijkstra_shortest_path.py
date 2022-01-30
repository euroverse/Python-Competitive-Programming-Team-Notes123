import heapq

''' [ Dijkstra Shortest Path ]
- 다익스트라 최단경로 알고리즘 : 출발 노드로부터 다른 모든 노드로 가는 최단경로를 계산

1. 출발 노드 설정
2. 최단거리 테이블 초기화
반 | 3. 방문하지 않은 노드중에서 최단거리가 가장 짧은 노드를 선택 (선형탐색)
복 | 4. 해당 노드를 고려하여 테이블 갱신
=> 매 반복마다 하나의 노드에 대한 최단 거리 확정됨.

3번의 선형탐색 과정을 힙을 이용해 간소화하면, O(V^2)=>O(ElogV)
'''
def dijkstra(start):
    # Set the start node.
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    
    while heap:
        # 최단거리가 가장 짧은 노드 선택 => now노드는 dist로 최단거리가 확정됨.
        dist, now = heapq.heappop(heap)
        
        # 이미 확정된 노드는 건너뜀.
        # if in_sack[now] == True: continue
        if distance[now] < dist:
            continue
            
        # 현재 노드의 인접 노드들에 대하여, 
        for vertex_num, edge_w in graph[now]:
            cost = dist + edge_w    # 현재 노드의 거리 + 간선 가중치
            
            if cost < distance[vertex_num]:
                distance[vertex_num] = cost
                heapq.heappush(heap, (cost, vertex_num))

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [int(1e9)] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))    # 인접노드 번호와 거리

dijkstra(start)
for i in range(1, n + 1):
    if distance[i] == int(1e9):
        print("INFINITY")
    else:
        print(distance[i])

'''
[Input Example 1]
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
[Output Example 1]
0
2
3
7
INFINITY
'''
