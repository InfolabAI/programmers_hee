#def solution(maps):
#    return
# 240405 정답.
from collections import deque
import numpy as np
def print_map(maps):
    for i in range(len(maps)):
        for v in maps[i]:
            print(f'{v:2}', end=' ')
        print()


def solution(maps):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    N = len(maps) # NOTE 틀린 부분. nxm 임, mxm 이 아님.
    M = len(maps[0]) # NOTE 틀린 부분. nxm 임, mxm 이 아님.
    
    # pad maps
    pmaps = []
    for i in range(N+2):
        if i == 0 or i==N+1:
            row = [0]*(M+2)
        else:
            row = [0]+maps[i-1]+[0]
        pmaps.append(row)
    visited = np.array([[0]*(M+2)]*(N+2))
    
    # search
    queue = deque([(1,1,1)])
    while queue:
        x, y, l = queue.popleft()
        if (x,y) == (N, M):
            return l
        for i in range(4):
            nx, ny, nl = x + dx[i], y + dy[i], l+1
            if pmaps[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny, nl))
                visited[nx][ny] = nl  # NOTE 틀린 부분. visited 수정을 queue 에서 뺄때 하는 것이 아니라 queue 에 append 할 때 하면 훨씬 빨라져서 효율성 테스트 통과함
        #print(queue)
        #print_map(visited)
        #print()
    return -1
    
    




















#from collections import deque
#
#dr = [1, -1, 0, 0]
#dc = [0, 0, 1, -1]
#    
#def solution(maps):
#    N = len(maps[0]) # 행 크기
#    M = len(maps) # 열 크기
#    visited = [[0 for _ in range(N)] for _ in range(M)]
#    visited[0][0] = 1
#    
#    queue = deque()
#    queue.append((0, 0))
#    
#    while len(queue) :
#        r, c = queue.popleft()
#        for i in range(4) :
#            nr, nc = r + dr[i], c + dc[i]
#            if nr < 0 or nr >= M or nc < 0 or nc >= N :
#                continue
#            if maps[nr][nc] == 1 and visited[nr][nc] == 0:
#                visited[nr][nc] = visited[r][c] + 1
#                queue.append((nr, nc))
#        
#    if visited[M-1][N-1] == 0 :
#        return -1
#    return visited[M-1][N-1]

#from collections import deque
#
#dr = [1, -1, 0, 0]
#dc = [0, 0, 1, -1]
#    
#def solution(maps):
#    M = len(maps[0])
#    N = len(maps)
#    visited = [[0 for _ in range(M)] for _ in range(N)]
#    
#    queue = deque([(0,0)])
#    visited[0][0] = 1
#    while queue:
#        r, c = queue.popleft()
#        for i in range(4):
#            nr, nc = r + dr[i], c + dc[i]
#            if nr >= N or nr < 0 or nc >= M or nc < 0:
#                continue
#            if visited[nr][nc] == 0 and maps[nr][nc] == 1:
#                queue.append((nr, nc))
#                visited[nr][nc] = visited[r][c] + 1
#    return visited[N-1][M-1] if visited[N-1][M-1] != 0 else -1

