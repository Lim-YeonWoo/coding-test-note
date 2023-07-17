'''
[DFS]
    * 알고리즘
        1. 시작노드 스택에 삽입 & 방문처리
        2. 스택 최상단 노드와 인접한 노드 중에
            방문하지 않은 것이 있으면, 스택에 삽입 & 방문처리
            이미 다 방문 했다면, pop()
        3. 2번 과정 끝까지 반복

    * 실제 구현
        : 구현시엔 스택으로 안함. 재귀함수로 구현.
        : 그래프 표현 방식은 "인접 리스트"
        : visited = [False] * (총 노드 수 + 1)
          이 visited 배열에 방문표시

    * 시간 복잡도
        O(N), N은 데이터 개수
'''

''' dfs function '''
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v)

    # 현재 노드와 인접한 노드 순차탐색
    for i in graph[v]:
        # 방문하지 않았다면, 재귀함수 호출
        if visited[i] == False :
                dfs(graph, i, visited)

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
dfs(graph, 1, visited) # 시작 노드는 1