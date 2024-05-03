#def solution(k, dungeons):
#    return 0
# 240227
from collections import deque
def BFS(tot, dgs):
    answer = 0
    queue = deque([(-1, tot, 0, [])])
    while queue:
        id, cur, consume, route = queue.popleft()
        cur = cur - consume
        answer = max(answer, len(route))
        for i, dg in enumerate(dgs):
            nreq, nconsume = dg
            if i not in route and cur >= nreq:
                queue.append((i, cur, nconsume, route + [i]))
        #print(id, cur, consume, route)
    return answer
        
def solution(k, dungeons):
    return BFS(k, dungeons)








## 완전 탐색
#from itertools import permutations
#
#def solution(k, dungeons):
#    answer = -1
#    candidates = list(permutations([x for x in range(len(dungeons))], len(dungeons)))
#
#    for candidate in candidates:
#        temp, cnt = k, 0
#        for idx in candidate:
#            if temp >= dungeons[idx][0]:
#                temp -= dungeons[idx][1]
#                cnt += 1
#        answer = max(answer, cnt)
#
#    return answer

## BFS
#from collections import deque
#
#def solution(k, dungeons):
#    answer = -1
#    queue = deque()
#    queue.append((k, []))
#
#    while queue:
#        k, route = queue.popleft()
#        for i in range(len(dungeons)):
#            a, b = dungeons[i]
#            if k >= a and i not in route:
#                temp = route + [i]
#                queue.append((k - b, temp))
#            else:
#                answer = max(answer, len(route))
#
#    return answer

# 240118 버전
#from collections import deque
#def BFS(k, dungeons):
#    queue = deque([[k, []]])
#    max_n = 0
#    while queue:
#        cur_k, route = queue.popleft()
#        max_n = max(max_n, len(route))
#        
#        for i in range(len(dungeons)):
#            k_limit, k_loss = dungeons[i]
#            if cur_k >= k_limit and i not in route:
#                queue.append([cur_k - k_loss, route + [i]])
#    return max_n
#
#def solution(k, dungeons):
#    return BFS(k, dungeons)

# 240116 버전
#from collections import deque
#def BFS(hp, dungeons):
#    max_d = 0
#    #for k in range(len(dungeons)): # 틀린 부분: 굳이 dungeons for 문 돌 필요없이, route 를 [] 로 지정하면 됨
#    #    queue = deque([[hp, [k]]]) # 틀린 부분
#    queue = deque([[hp, []]])
#    #print(f"start {k}")
#    while queue:
#        hp, route = queue.popleft()
#        max_d = max(max_d, len(route))
#        #print(index, hp, route, "->", queue)
#        for i in range(len(dungeons)):
#            hp_limit, hp_loss = dungeons[i]
#            if i not in route and hp >= hp_limit:
#                queue.append([hp - hp_loss, route+[i]])
#
#    return max_d
#    
#def solution(k, dungeons):
#    return BFS(k, dungeons)

# 240115 버전 (틀림)
#from collections import deque
#def BFS(st, eg, dungeons):
#    visited = [0 for _ in dungeons]
#    queue = deque([[None, eg, 0]])
#    max_num = 0
#    while queue:
#        st, eg, num = queue.popleft()
#        max_num = max(num, max_num)
#        print(st, eg, num, max_num)
#        if st is not None:
#            visited[st] = 1
#        for nt in range(len(dungeons)): # 틀린 부분. visited 가 아님.
#            eg1, eg2 = dungeons[nt]
#            if eg >= eg1 and visited[nt] == 0:
#                queue.append([nt, eg - eg2, num + 1])
#    
#def solution(k, dungeons):
#    BFS(0, k, dungeons)
#    return 0

## 231206 버전 BFS 연습 
#from collections import deque
#def solution(k, dungeons):
#    root = (k, [])
#    queue = deque([root])
#    answer = -1
#    while queue:
#        k, route = queue.popleft()
#        for i in range(len(dungeons)):
#            a, b = dungeons[i]
#            if k >= a and i not in route:
#                next = (k - b, route + [i])
#                queue.append(next)
#            else:
#                answer = max(len(route), answer)
#    return answer

