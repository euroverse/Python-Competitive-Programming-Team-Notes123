''' [ Floyd-Warshall ]
- 플로이드 워셜 알고리즘 : 모든 노드에서 다른 모든 노드까지의 최단경로를 계산한다.
- 구현이 쉽지만, 시간 복잡도가 O(N^3)라서 노드의 갯수가 적을 때 사용한다.
- " A에서 B로 가는 경로에 대해, K를 거쳐 가는 경우를 고려한다 "
'''
def floyd_warshall():
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

n, m = map(int, input().split())
graph = [[int(1e9)] * (n+1) for _ in range(n+1)]

# 출발 노드와 도착 노드가 같은 경우, 최단거리 = 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b: graph[a][b] = 0

# 간선 입력
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a][b] = w

# 출력
floyd_warshall()
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == int(1e9): print("-1", end=" ")
        else: print(graph[a][b], end=" ")
    print()
    
'''
[Input Example 1]
5 6
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
[Output Example 1]
0     2     3     7     -1
-1    0     4     5     -1
-1    -1    0     6     -1
-1    -1    -1    0     -1
1     3     4     8      0
'''