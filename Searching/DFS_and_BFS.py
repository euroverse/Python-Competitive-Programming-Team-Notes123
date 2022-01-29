from collections import deque

''' Depth First Search (DFS)
https://youtu.be/1vLqC1rItM8?list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
2. 스택의 최상단 노드 (방금 방문한 노드)의
   방문하지 않은 인접 노드를 차례로 스택에 삽입하고 방문 처리
3. 방문하지 않은 인접 노드가 없는 경우 최상단 노드 꺼내기
4. 2번과 3번 반복
=> 스택 대신 재귀 함수를 이용하여 구현 (아래 소스 코드)
'''
def dfs(x):
    print(x, end=' ')
    visited[x] = True
    for y in graph[x]:
        if not(visited[y]):
            dfs(y)

''' Breadth First Search (BFS) '''
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

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for e in graph:
    e.sort()

visited = [False] * (n + 1)
dfs(start)
print()
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
1 2 4 3 
1 2 3 4
'''
