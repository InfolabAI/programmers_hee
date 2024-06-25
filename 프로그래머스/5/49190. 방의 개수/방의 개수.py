def solution(arrows):
    return
# 240625
# 다시 풀기
# Q: map 을 어떤 개념으로 생각할 것인가? 매우 커질 수 있음.
# A: 생각할 필요없음. visited 만 생각하면 됨.
# Q: 방을 어떻게 셀 것인가? 그냥 세면 너무 비효율적임
# A: 어떤 이미 방문한 점에 다른 경로로 다시 방문하면 방이 하나 더 생김.
d = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
def move1(a, st, map_, room):
    dt = (st[0] + d[a][0], st[1] + d[a][1])
    map_[str(st)] += [str(dt)]
    
    if str(st) not in map_[str(dt)] and len(map_[str(dt)])>0:
        map_[str(dt)] += [str(st)] # NOTE 틀린 부분. in > out, out > in 모두 저장해야 중복된 방 갯수 증가를 피할 수 있음.
        return room+1, dt
    else:
        map_[str(dt)] += [str(st)]
        return room, dt
        
    # 예)
    # 1. (0,0) -> (1,0) 이동 시, (0,0)(1,0) out, (1,0)(0,0) in.
    # 2. (1,1) -> (0,0) 이동 시, (1,1)(0,0) out, (0,0)(1,1) in. 이때, (0,0) out 이 1이므로, 방 1개 추가
    # 3. (0,0) -> (1,-1) 이동 시, (0,0)(1,-1) out, (1,-1)(0,0) in.
    # 3. (0,1) -> (0,0) 이동 시, (0,1)(0,0) out, (0,0)(0,1) in. 이때, (0,0) out 이 2이므로, 방 1개 추가
    # 상관없네. out 이 1 이상이면 out 과 동일하지 않은 in 발생시 무조건 방 1개 추가하면 됨. 즉, map_ 에는 out 만 저장.
    
    
from collections import defaultdict
def solution(arrows):
    st = (0, 0)
    map_ = defaultdict(list)
    room = 0
    for a in arrows:
        room, st = move1(a, st, map_, room)
        #print(st, room, dict(map_))
        room, st = move1(a, st, map_, room)
        #print(st, room, dict(map_))
    
    return room























#from collections import deque, defaultdict
#
#def solution(arrows):
#    answer= 0
#    visited = defaultdict(int)
#    visited_dir = defaultdict(int)
#    move = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
#    now = (0,0)
#    queue = deque([now])
#    
#    for i in arrows:
#        for _ in range(2):
#            next = (now[0] + move[i][0], now[1] + move[i][1])
#            queue.append(next)
#            now = next
#            
#    now = queue.popleft()
#    visited[now] = 1
#    while queue:
#        next = queue.popleft()
#        if visited[next] == 1:
#            if visited_dir[(now, next)] == 0:
#                answer += 1
#        else:
#            visited[next] = 1
#    
#        visited_dir[(now, next)] = 1
#        visited_dir[(next, now)] = 1
#        now = next
#        
#    return answer











#import collections
#def solution(arrows):
#    answer = 0
##    move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
#
#    move = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
#    now = (0, 0)
#
#    # visited : 노드 방문 체크
#    # visited_dir : 노드 방문 경로 체크 ((A, B)는 A -> B 경로를 의미)
#    visited = collections.defaultdict(int)
#    visited_dir = collections.defaultdict(int)
#
#    # arrows 따라 노드 좌표를 큐에 추가
#    queue = collections.deque([now])
#    for i in arrows:
#        # 모래 시계 형태 예외를 처리하기 위해 해당 방향으로 2칸씩 추가한다
#        for _ in range(2):
#            next = (now[0] + move[i][0], now[1] + move[i][1])
#            queue.append(next)
#            now = next
#
#    now = queue.popleft()
#    visited[now] = 1
#
#    while queue:
#        next = queue.popleft()
#
#        # 이미 방문한 노드(visited[x]==1)인 경우
#        if visited[next] == 1:
#            # 해당 경로로 처음 들어온 경우인 경우 answer++
#            # 처음 들어온 경우에 방이 처음 생성되므로!
#            if visited_dir[(now, next)] == 0:
#                answer += 1
#        # 처음 방문한 노드인 경우 방문 체크를 한다
#        else:
#            visited[next] = 1
#
#        # 해당 노드로 들어온 경로를 방문 체크해준다
#        visited_dir[(now, next)] = 1
#        visited_dir[(next, now)] = 1
#        now = next
#
#    return answer

# 240621
#from collections import defaultdict
#d = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]
#def out_to_in(a):
#    # 나갈때의 방향이 아니라 들어올 때의 방향으로 변환 후 저장해야 함
#    return a-4 if a-4 >= 0 else a+4
#
#def room_check(st, a, vt, vt_path):
#    nt = [st[0] + d[a][0], st[1] + d[a][1]]
#    ret = False
#    if vt[(nt[0], nt[1])] >= 1:
#        if vt_path[(nt[0], nt[1], a)] == 0:
#            ret = True
#    vt[(st[0], st[1])] += 1
#    vt_path[(st[0], st[1], out_to_in(a))] = 1 # st 에서 나가는 것 # NOTE 틀린 부분. st 에서 나가는 것과 nt 로 들어오는 것 모두를 save 해야 함
#    vt_path[(nt[0], nt[1], a)] = 1 # nt 에게 들어오는 것
#    return ret, nt
#        
#def solution(arrows):
#    st = [0,0]
#    vt = defaultdict(lambda :0)
#    vt_path = defaultdict(lambda :0)
#    #vt[(0,0)] = 1
#    answer = 0 
#    for a in arrows:
#        #print(st, end=f" >{a}> ")
#        # first
#        ret, st = room_check(st, a, vt, vt_path)
#        if ret:
#            answer += 1
#        #print(f"{answer} nt {st}", f"vt {vt.items()} vt_path {vt_path.items()}\n")
#        
#        #print(st, end=f" >{a}> ")
#        # second
#        ret, st = room_check(st, a, vt, vt_path)
#        if ret:
#            answer += 1
#        #print(f"{answer} nt {st}", f"vt {vt.items()} vt_path {vt_path.items()}\n")
#    
#    return answer
