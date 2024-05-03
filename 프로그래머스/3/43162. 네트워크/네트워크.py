#def solution(n, computers):
#    return
# 240409. 정답. 10m.
from collections import defaultdict
def solution(n, computers):
    edges = defaultdict(list)
    for st, row in enumerate(computers):
        for dt, val in enumerate(row):
            if val == 1 and st != dt:
                edges[st] += [dt]
                
    visited = [0] * n
    answer = 0
    for i in range(n):
        if visited[i] == 0:
            answer += 1
            stack = [i]
            visited[i] = 1
            while stack:
                #print(stack, answer)
                curn = stack.pop()
                for nextn in edges[curn]:
                    if visited[nextn] == 0:
                        stack.append(nextn)
                        visited[nextn] = 1
        
    return answer














# def solution(n, computers):
#     visited = [0 for _ in range(n)]
#     def dfs(start):
#         #pop을 언제하는데?
#         #dfs 인자는 뭔데? 왜 그런데?
#         stack = [start]
#         while stack:
#             k = stack.pop()
#             if visited[k] == 0:
#                 visited[k] = 1
#             for i in range(n):
#                 #왜 visited[k] 가 아니라 visited[i] 인데?
#                 if computers[k][i] == 1 and visited[i] == 0:
#                     #왜 stack append 인데?
#                     stack.append(i)
#                     
#     #visited = 0
#     i = 0
#     ans = 0
#     while 0 in visited:
#         #while 밑에 왜 if 문이 필요한데?
#         if visited[i] == 0:
#             dfs(i)
#             ans+=1
#         i+=1
#     return ans



# deque 버전
#from collections import deque
#def solution(n, computers):
#    visited = [0 for _ in range(n)]
#    def dfs(start):
#        stack = deque([start])
#        while stack:
#            i = stack.pop()
#            if visited[i] == 0: visited[i] = 1
#            for j, edge in enumerate(computers[i]):
#                if edge == 1 and visited[j] == 0:
#                    stack.append(j)
#                
#        
#    start = 0
#    ans = 0
#    while 0 in visited:
#        dfs(start)
#        ans += 1
#        try:
#            start = visited.index(0)
#        except:
#            break
#        
#    return ans

# ValueError: 0 is not in list
# start = visited.index(0)

#from collections import deque
#import numpy as np
#def solution(n, computers):
#    visited = [0 for i in range(n)]
#    
#    def dfs(start):
#        stack = deque([start])
#        while stack:
#            cur = stack.pop()
#            print(cur)
#            if visited[cur] == 0:
#                visited[cur] = 1
#            for i in range(n):
#                if computers[cur][i] == 1 and visited[i] == 0:
#                    stack.append(i)
#                    
#    k = 0
#    num_graphs = 0
#    while np.array(visited).sum() != n:
#        if visited[k] == 0:
#            dfs(k)
#            num_graphs += 1
#        k += 1
#    return num_graphs

