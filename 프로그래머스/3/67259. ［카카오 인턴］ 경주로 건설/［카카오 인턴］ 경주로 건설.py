def pad_251023(b):
    Y, X = len(b), len(b[0])
    map1 = [[1 for _ in range(X+2)] for _ in range(Y+2)]
    for x in range(X):
        for y in range(Y):
            map1[x+1][y+1] = b[x][y]
    return map1

from collections import deque
def bfs_251023(b, dr):
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    Y, X = len(b), len(b[0])
    visited = [[1000000000 for _ in range(X)] for _ in range(Y)]
    queue = deque([(1, 1, dr, 0)])
    while True:
        cx, cy, cdr, ccost = queue.popleft()
        #print(cx, cy, cdr, ccost, queue)
        for ndr in d:
            nx, ny = cx + ndr[0], cy + ndr[1]
            if cdr == ndr:
                ncost = ccost + 100
            else:
                ncost = ccost + 600
                
            if b[nx][ny] == 0 and ncost < visited[nx][ny]:
                queue.append((nx, ny, ndr, ncost))
                visited[nx][ny] = ncost
                
            #print(nx, ny, ndr, ncost, queue, visited[nx][ny], b[nx][ny])
        if len(queue) == 0:
            break
            
    return visited[X-2][Y-2]
            
def solution_251023(board):
    return min(bfs_251023(pad_251023(board), (0, 1)), bfs_251023(pad_251023(board), (1, 0)))
    
    
#########################
#########################
#########################

def printm(board):
    # board(2차원 리스트)의 내용을 한 줄씩 출력하는 함수 (디버깅용)
    for row in board:
        # board의 각 행(row)을 순회합니다.
        print(row)
        # 현재 행(row)을 출력합니다.
        
def pad(b):
    # 원본 board(b)의 외곽에 1(벽)으로 된 테두리를 추가하는 함수
    # 이는 BFS 탐색 시 경계(edge) 체크를 따로 할 필요가 없게 만듭니다.
    newb = []
    # 테두리가 추가된 새 board(newb)를 저장할 리스트 초기화
    for i in range(len(b)+2):
        # 새 board의 행 크기(원본 크기 + 2)만큼 반복 (위아래 테두리 포함)
        if i == 0 or i == len(b)+1:
            # 첫 번째 행(i=0)이나 마지막 행(i=len(b)+1)인 경우 (위아래 테두리)
            newb.append([1 for _ in range(len(b)+2)])
            # (원본 열 크기 + 2)만큼 1로 채워진 리스트를 newb에 추가 (벽으로 채움)
        else:
            # 테두리가 아닌, 원본 board 내용이 들어갈 행인 경우
            newb.append([1] + b[i-1] + [1])
            # [1] (왼쪽 벽) + 원본 board의 (i-1)번째 행 + [1] (오른쪽 벽)을 합쳐 newb에 추가
    return newb
    # 테두리가 추가된 newb를 반환
        
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 이동 방향을 나타내는 튜플 리스트 (0: 우, 1: 하, 2: 좌, 3: 상)
from collections import deque
# BFS를 효율적으로 수행하기 위해 deque(양방향 큐) 자료구조를 import

# 240722 (작성일 주석)
def bfs(board, dr):
    # BFS를 수행하여 최소 비용을 찾는 함수. 
    # board(테두리가 추가된)와 초기 방향(dr: 0 또는 1)을 인자로 받음.
    st = (1,1)
    # 시작 위치. 원본 (0,0)이었지만 pad 함수로 인해 (1,1)이 됨.
    #printm(board) # (디버깅용) 테두리가 추가된 board 출력 (현재 주석 처리됨)
    X, Y = len(board), len(board[0])
    # board의 행(X)과 열(Y) 크기를 저장
    visited = [[9999999 for _ in range(Y)] for _ in range(X)]
    # 각 칸에 도달하는 '최소' 비용을 저장할 2차원 리스트. 
    # 매우 큰 값(9999999)으로 초기화하여 아직 방문하지 않았거나 더 비싼 비용으로 방문했음을 표시.
    
    queue = deque([(st[0], st[1], dr, 0)]) # st, dr, cost # NOTE...
    # BFS를 위한 deque 초기화. (x좌표, y좌표, 현재 방향, 현재까지 비용)을 튜플로 묶어 리스트에 넣고 deque 생성.
    # NOTE (개발자 메모): deque를 초기화할 때 [(...)] 처럼 리스트로 감싸야 튜플 자체가 하나의 원소로 들어감.
    
    while len(queue) > 0:
        # queue에 탐색할 노드(경로)가 남아있는 동안 반복
        x, y, dr, cost = queue.popleft()
        # queue의 맨 앞에서 탐색할 노드 정보(위치, 이전 방향, 현재 비용)를 꺼냄
        
        for i in range(4):
            # 4가지 방향(0~3: 우, 하, 좌, 상)에 대해 반복
            nx, ny = x + d[i][0], y + d[i][1]
            # 현재 위치(x, y)에서 i번째 방향으로 이동한 다음 위치(nx, ny) 계산
            
            ncost = 100 + cost if dr == i else 600 + cost
            # 다음 비용(ncost) 계산:
            # 이전 방향(dr)과 현재 방향(i)이 같으면 -> 직선 도로. 비용 +100
            # 이전 방향(dr)과 현재 방향(i)이 다르면 -> 코너 발생. 비용 +100(직선) +500(코너) = +600
            
            if ncost < visited[nx][ny] and board[nx][ny] == 0:
                # 1. 계산된 비용(ncost)이 해당 위치(nx, ny)에 기록된 기존 최소 비용(visited[nx][ny])보다 작고,
                # 2. 다음 위치(nx, ny)가 벽(1)이 아닌 경우 (0인 경우)
                
                queue.append((nx, ny, i, ncost))
                # queue에 다음 탐색 정보(새 위치, 새 방향, 새 비용)를 추가
                visited[nx][ny] = ncost
                # 해당 위치(nx, ny)의 최소 비용을 ncost로 갱신
                
    #print(queue, len(queue), i) # (디버깅용) 현재 queue 상태 출력 (현재 주석 처리됨)
    return visited[X-2][Y-2]
    # (X-2, Y-2) (테두리를 제외한 실제 도착점, 원본의 (N-1, N-1))까지의 최소 비용을 반환
        

# 240715 (작성일 주석)
def solution_240715(board):
    # 문제의 메인 함수. board를 입력받아 최소 건설 비용을 반환
    answer = 0
    # (사용되지 않는 변수) answer를 0으로 초기화
    
    # 시작점 (1,1)에서는 오른쪽(방향 0)으로 가거나 아래쪽(방향 1)으로 가는 두 가지 경우만 의미가 있음.
    # (왼쪽/위쪽은 벽이거나 시작점이므로)
    return min(bfs(pad(board), 0), bfs(pad(board), 1))
    # board에 테두리를 추가(pad(board))한 후,
    # 1. 처음 방향을 0(우측)으로 설정하고 BFS를 실행한 비용
    # 2. 처음 방향을 1(아래)로 설정하고 BFS를 실행한 비용
    # 위 두 가지 경우 중 더 작은 값을 최종 결과로 반환.



# ref
#from collections import deque
#def solution(board):
#    def bfs(start):
#        direc = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]} # 북,동,남,서 순서
#        length = len(board)
#        visited = [[987654321]*length for _ in range(length)]
#        visited[0][0] = 0
#
#        q = deque([start]) # x, y, cost, dir
#        while q:
#            x, y, cost, d = q.popleft()
#            for i in range(4): # 북,동,남,서 순서
#                nx = x + direc[i][0]
#                ny = y + direc[i][1]
#
#                # board 안에 있고, 벽이 아닌지 확인
#                if 0 <= nx < length and 0 <= ny < length and board[nx][ny] == 0:
#                    
#                    # 비용계산
#                    if i == d : ncost = cost + 100
#                    else : ncost =  cost + 600
#                    # 최소 비용이면 갱신 후 endeque!
#                    if ncost < visited[nx][ny]:
#                        visited[nx][ny] = ncost
#                        q.append([nx, ny, ncost, i])
#                        
#        return visited[-1][-1]
#    
#    print([bfs((0, 0, 0, 1)), bfs((0, 0, 0, 2))])
#    return min([bfs((0, 0, 0, 1)), bfs((0, 0, 0, 2))])


#  240625
# 직선인지 코너인지를 어떻게 모델링할 것인가? 완료
# NOTE 틀린부분. visited 를 사용하면, BFS 라고해도 최단 경로가 먼저 방문한 노드를 다시 방문하지 않기 때문에 최소 비용인 경로가 잘려버리는 사태가 발생하는데 어떻게 해결할 것인가? A: visited 는 최소비용을 update 하고, route 로 재방문을 금지하면 해결되나, 너무 느림.
# NOTE 틀린부분. 느린 문제를 어떻게 해결할 것인가? A: route 제외하고, visited 가 최소비용인지만 비교해서 queue 를 update 하면 됨.
# NOTE 틀린부분. 최소비용을 계산할때, 현재상태만 보면 안됨. 현재는 같은 비용일지라도, 직선으로 통과하는지, 커브로 통과하는지에 따라, 다음 셀에서 비용이 달라짐. 심지어, 현재 셀에서 비용이 100원 크더라도, 직선이라 다음셀에서 500원을 아낀다면 최소 비용이 됨. A: BFS 의 state 가 [x, y, cost, pdr] 을 가지고, 일반적인 BFS 를 돌 되, 시작 조건의 pdr 이 아래쪽, 오른쪽일 때를 둘 다 계산해서 min 값을 가져오는 것이 핵심.

#from collections import deque
#ds = {0: (0,1), 1: (1,0), 2: (0, -1), 3: (-1, 0)}
#def costf(pd, d):
#    if pd == d: # 직선
#        return 100
#    else: # 코너
#        return 500 + 100 # NOTE 틀린 부분. 코너일때도 직선 도로 비용 1번 내야함.
#    
#def pad(b):
#    newb = []
#    for i in range(len(b)+2):
#        if i == 0 or i == len(b)+1:
#            newb.append([1 for _ in range(len(b)+2)])
#        else:
#            newb.append([1] + b[i-1] + [1])
#    return newb
#        
#    
#def bfs(board, start):
#    # start == [x, y, cost, pdr]
#    #printm(board)
#    visited = [[99999999 for _ in range(len(board[0]))] for _ in range(len(board))] # NOTE 틀린 부분. visited 가 0,1 이 아니라, 최소비용을 담고, update 하는 식으로 진행하면 됨.
#    visited[start[0]][start[1]] = 100
#    queue = deque([start])
#    while queue:
#        x, y, cost, pdr = queue.popleft()
#        for dr, _ in ds.items():
#            ncost = cost+costf(pdr, dr)
#            nx, ny = x + ds[dr][0], y + ds[dr][1]
#            #print(nx, ny, ncost, dr, visited[nx][ny])
#            if board[nx][ny] == 0 and ncost < visited[nx][ny]:
#                queue.append([nx, ny, ncost, dr])
#                visited[nx][ny] = ncost
#        #print(queue)
#    #printm(visited)
#    return visited[-2][-2]
#    
#def solution(board):
#    answer = 0
#    X, Y = len(board), len(board[0])
#    return min(bfs(pad(board), [1,1,0,0]), bfs(pad(board), [1,1,0,1]))




def solution(board):
    answer = 0
    #return solution_240715(board)
    return solution_251023(board)