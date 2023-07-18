'''
[BFS]
    * 알고리즘
        1. 시작 노드를 queue에 append & 방문처리
        2. queue에서 노드 pop(), 그것과 인접하는 모든 노드 append()
        3. 2번 과정 끝까지 반복

    * 실제 구현
        : from collections import deque
        : q = deque([start]) # start만 들은 list를 deque로 변경
        : while q: # 큐가 빌 때까지 반복

    * 시간 복잡도
        O(N), N은 데이터 개수.
        보통 DFS보다 수행시간 좋은 편.
'''

''' bfs function '''
from collections import deque

def bfs(graph, start, visited):
    # [1] 큐 생성 & start 넣고 방문 표시
    q = deque([start])
    visited[start] = True

    # [2] 큐가 빌 때까지 while문 돌기
    while q :
        # [2-1] 큐에서 빼기
        v = q.popleft()
        print(v)

        # [2-2] 인접한 모든 노드 중 방문 안한거 전부 큐에 넣기
        for i in graph[v]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True

''' grpah 표현 (인접 리스트) '''
graph = [
    [], #노드0 없으니까 비워두기
    [2, 3, 8], #1과 인접한 노드들
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

''' visited 배열 초기화 '''
visited = [False] * 9

''' dfs 호출 '''
bfs(graph, 1, visited) # 시작 노드는 1
