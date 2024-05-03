#def solution(rectangle, characterX, characterY, itemX, itemY):
#    return 0
# 240220
from collections import deque
import numpy as np

TIMES = 2
MAX   = 51 * TIMES

def inner_to_zero(graph, x1, y1, x2, y2):
    graph[x1+1:x2, y1+1:y2] = 0
    return graph
    
def line_to_one(graph, x1, y1, x2, y2):
    graph[x1:x2+1, y1] = 1
    graph[x1:x2+1, y2] = 1
    graph[x1, y1:y2+1] = 1
    graph[x2, y1:y2+1] = 1
    return graph
    
def BFS(graph, cx, cy, ix, iy): # NOTE 틀린 부분, DFS 로 하면 틀리고, BFS 로 하면 맞음
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = np.zeros((MAX, MAX), dtype=int)
    stack = deque([(cx, cy, 0)])
    while stack:
        x, y, dist = stack.popleft()
        #print(x,y)
        visited[x, y] = 1
        if x == ix and y == iy:
            break
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if graph[nx, ny] == 1 and visited[nx, ny] == 0:
                stack.append((nx, ny, dist+1))
    return dist//TIMES

def solution(rectangle, characterX, characterY, itemX, itemY):
    rt = np.array(rectangle)
    rt = rt*TIMES
    characterX, characterY, itemX, itemY = characterX*TIMES, characterY*TIMES, itemX*TIMES, itemY*TIMES
    graph = np.zeros((MAX, MAX), dtype=int)
    for r1 in rt:
        line_to_one(graph, *r1)
    for r1 in rt:
        inner_to_zero(graph, *r1)
    dist = BFS(graph, characterX, characterY, itemX, itemY)
    #print(dist)
    #for i, row in enumerate(graph):
    #    print(i, list(row))
    
    return dist


















# 240104 ver. BFS 를 나중에 짜는 것이 맞음. 먼저 짜면 테스트를 못하잖아.
#def BFS(sX, sY, iX, iY, graph):
#    """
#    sX, sY, eX, eY, graph 는 2배 처리됨
#    """
#    directionX = [-1, 1, 0, 0]                             # NOTE direction 이 왜 이것인지 확인, 여기서 BFS 틀림. 
#    directionY = [0, 0, -1, 1]                              
#    visited = [[0] * 102 for _ in range(102)] # 시작이 1 인 index 처리를 위해 원래 [51,51] 이라 가정함
#    visited[sX][sY] = 1
#    
#    queue = deque([[sX, sY, 1]]) # 시작위치, dist
#    while queue:
#        x, y, dist = queue.popleft()
#        if x == iX and y == iY:
#            return dist
#        for i in range(4):
#            nX, nY = x+directionX[i], y+directionY[i]
#            if nX <= 102 and nX >= 0 and nY <= 102 and nY >= 0:
#                if visited[nX][nY] == 0 and graph[nX][nY] == 1:
#                    queue.append([nX, nY, dist+1])
#                    visited[nX][nY] = 1
#    return 0
#
#def solution(rectangle, characterX, characterY, itemX, itemY): # solution 도 잘못됨
#    answer = 0
#    times = 2
#    graph = [[5] * 51*times for _ in range(51*times)] # NOTE 틀린 부분. 5로 초기화 하는 이유는 사각형 내부와 외부를 구분하기 위함.
#    for i, (lX, lY, rX, rY) in enumerate(rectangle):
#        lX, lY, rX, rY = lX*times, lY*times, rX*times, rY*times
#        for row in range(lX, rX+1): # NOTE 틀린 부분. 사각형 내부에는 라인이 없어야 하는데 이를 어기고 라인을 내부에 그리면 정답보다 빠른 루트로 오답이 됨
#            for col in range(lY, rY+1):
#                if lX < row < rX and lY < col < rY:
#                    graph[row][col] = 0
#                elif graph[row][col] != 0: # DP 가 됨. 이전에 계산으로 0이 된 내부를 이용하는 것.
#                    graph[row][col] = 1
#        
#    #for row in graph:
#    #    print(row)
#        
#    
#    return BFS(characterX*times, characterY*times, itemX*times, itemY*times, graph) // times # NOTE 틀린 부분. times 로 다시 나눠야 함.
























#from collections import deque
#
#def BFS(startX, startY, endX, endY, graph):
#    dx = [-1, 1, 0, 0]                              # 상하좌우순
#    dy = [0, 0, -1, 1]                              # 상하좌우순
#    visited = [[False] * 102 for _ in range(102)]   # 방문여부 2배 확장
#    visited[startX][startY] = True                  # 시작지점 방문여부 True
#    
#    queue = deque([(startX, startY, 1)])            # (x, y, dist), dist 1부터 시작
#    while queue:
#        x, y, dist = queue.popleft()
#        if x == endX and y == endY:                 # 아이템에 도달하면
#            return dist                             # 이동거리 반환
#        
#        for i in range(4):
#            nx = x + dx[i]
#            ny = y + dy[i]
#            if 0 <= nx < 102 and 0 <= ny < 102:                 # 그래프 범위 내
#                if graph[nx][ny] == 1 and not visited[nx][ny]:  # 테두리이면서, 방문한 적이 없으면
#                    visited[nx][ny] = True                      # 방문여부 True
#                    queue.append((nx, ny, dist + 1))            # 다음위치, 이동거리 + 1
#    return -1       # 목표지점에 도달할 수 없는 경우 -1 반환
    
    
#def solution(rectangle, characterX, characterY, itemX, itemY):
#    # ㄷ자 형태의 테두리의 경우, 평행한 두 테두리가 한 칸 차이일 때 방지
#    graph = [[5] * 102 for _ in range(102)]         # 2배 확장
#    for rect in rectangle:                          # 각 사각형의 좌표에 대해
#        x1, y1, x2, y2 = map(lambda x: x * 2, rect) # 2배 확장
#        for row in range(x1, x2 + 1):               # 현재 사각형의 Row 범위
#            for col in range(y1, y2 + 1):           # 현재 사각형의 Col 범위
#                if x1 < row < x2 and y1 < col < y2: # 현재 사각형의 내부인 경우
#                    graph[row][col] = 0             # 0 
#                elif graph[row][col] != 0:          # 현재 사각형의 테두리이면서, 다른 사각형의 내부가 아닌 경우
#                    graph[row][col] = 1             # 1
#    
#    # 2배 확장하였으므로, 시작지점 및 아이템위치 2배 확장
#    answer = BFS(characterX * 2, characterY * 2, itemX * 2, itemY * 2, graph)
#    return answer // 2      # 2배 확장하였으므로, 2배 축소하여 정답 반환

# 240105
#from collections import deque
#MAX = 51
#TIMES = 2
#
#def BFS(sx, sy, ix, iy, graph):
#    directionX = [1, -1, 0, 0]
#    directionY = [0, 0, 1, -1]
#    visited = [[0 for _ in range(MAX*TIMES)] for _ in range(MAX*TIMES)]
#    visited[sx][sy] = 1
#    queue = deque([[sx, sy, 0]])
#    while queue:
#        x, y, dist = queue.popleft()
#        #print(x, y, dist, end="   >>   ")
#        if x==ix and y==iy:
#            return dist
#        for i in range(4):
#            nx, ny = x+directionX[i], y+directionY[i]
#            if 0 <= nx < MAX*TIMES and 0 <= ny < MAX*TIMES:
#                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
#                    queue.append([nx, ny, dist+1])
#                    visited[nx][ny] = 1
#    return -1
#
#def solution(rectangle, characterX, characterY, itemX, itemY):
#    characterX, characterY, itemX, itemY = characterX*TIMES, characterY*TIMES, itemX*TIMES, itemY*TIMES
#    rectangle = [list(map(lambda x: x*TIMES, rec)) for rec in rectangle]
#    graph = [[5 for _ in range(MAX*TIMES)] for _ in range(MAX*TIMES)]
#    for x1, y1, x2, y2 in rectangle:
#        for x in range(x1, x2+1):
#            for y in range(y1, y2+1):
#                if x1 < x < x2 and y1 < y < y2:
#                    graph[x][y] = 0
#                elif graph[x][y] != 0:
#                    graph[x][y] = 1
#
#    ret = BFS(characterX, characterY, itemX, itemY, graph)
#    return ret // 2

