''' Depth First Search (DFS) with Stack or RecursiveFunction
https://youtu.be/1vLqC1rItM8?list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
2. 스택의 최상단 노드 (방금 방문한 노드)의 방문하지 않은 인접 노드 하나를 스택에 삽입하고 방문 처리
3. 방문하지 않은 인접 노드가 없는 경우 최상단 노드 꺼내기
4. 2번과 3번 반복
=> 스택 대신 재귀 함수를 이용하여 구현 가능 (아래 소스 코드)
'''

def dfs(x):
    print(x, end=' ')
    visited[x] = True
    for y in graph[x]:        # 최상단 노드 x의 인접 노드 y에 대해 DFS 수행
        if not(visited[y]):
            dfs(y)
            
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
'''
