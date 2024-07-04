def solution(board):
    answer = 0
    return answer

def print_map(board):
    for row in board:
        print(row)
        
#  240625 틀림.
# 직선인지 코너인지를 어떻게 모델링할 것인가? 완료
# NOTE 틀린부분. visited 를 사용하면, BFS 라고해도 최단 경로가 먼저 방문한 노드를 다시 방문하지 않기 때문에 최소 비용인 경로가 잘려버리는 사태가 발생하는데 어떻게 해결할 것인가? A: visited 는 최소비용을 update 하고, route 로 재방문을 금지하면 해결되나, 너무 느림.
# NOTE 틀린부분. 느린 문제를 어떻게 해결할 것인가? A: route 제외하고, visited 가 최소비용인지만 비교해서 queue 를 update 하면 됨.
# NOTE 틀린부분. 최소비용을 계산할때, 현재상태만 보면 안됨. 현재는 같은 비용일지라도, 직선으로 통과하는지, 커브로 통과하는지에 따라, 다음 셀에서 비용이 달라짐. 심지어, 현재 셀에서 비용이 100원 크더라도, 직선이라 다음셀에서 500원을 아낀다면 최소 비용이 됨.

from collections import deque
ds = {0: (0,1), 1: (1,0), 2: (0, -1), 3: (-1, 0)}
def costf(pd, d):
    if pd == d: # 직선
        return 100
    else: # 코너
        return 500 + 100 # NOTE 틀린 부분. 코너일때도 직선 도로 비용 1번 내야함.
    
def pad(b):
    newb = []
    for i in range(len(b)+2):
        if i == 0 or i == len(b)+1:
            newb.append([1 for _ in range(len(b)+2)])
        else:
            newb.append([1] + b[i-1] + [1])
    return newb
        
    
def bfs(board, start):
    # start == [x, y, cost, pdr]
    #print_map(board)
    visited = [[99999999 for _ in range(len(board[0]))] for _ in range(len(board))] # NOTE 틀린 부분. visited 가 0,1 이 아니라, 최소비용을 담고, update 하는 식으로 진행하면 됨.
    visited[start[0]][start[1]] = 100
    queue = deque([start])
    while queue:
        x, y, cost, pdr = queue.popleft()
        for dr, _ in ds.items():
            ncost = cost+costf(pdr, dr)
            nx, ny = x + ds[dr][0], y + ds[dr][1]
            #print(nx, ny, ncost, dr, visited[nx][ny])
            if board[nx][ny] == 0 and ncost < visited[nx][ny]:
                queue.append([nx, ny, ncost, dr])
                visited[nx][ny] = ncost
        #print(queue)
    #print_map(visited)
    return visited[-2][-2]
    
def solution(board):
    answer = 0
    X, Y = len(board), len(board[0])
    return min(bfs(pad(board), [1,1,0,0]), bfs(pad(board), [1,1,0,1]))
















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