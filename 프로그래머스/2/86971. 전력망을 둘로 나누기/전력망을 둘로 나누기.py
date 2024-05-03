#def solution(n, wires):
#    answer = 10000
#    return answer
# 240214 
from collections import defaultdict, deque
import numpy as np
def solution(n, wires):
    graph = defaultdict(list)
    wires = [[s-1, d-1] for s, d in wires]
    answer = 10000
    for s, d in wires:
        graph[s].append(d)
        graph[d].append(s)
    
    for s, d in wires:
        #print(s, d)
        visited = np.zeros((n))
        queue = deque([s])
        while queue:
            s = queue.popleft()
            visited[s] = 1
            for nd in graph[s]:
                if nd != d and visited[nd] == 0:
                    queue.append(nd)
        diff = abs(n - sum(visited) - sum(visited))
        answer = min(answer, diff)
        #print(s, queue, visited, answer)
                    
    
    return answer






















# Edge 별로 한쪽으로 DFS 하면서, 전체 갯수 - visited 가 가장 작은 edge 에서의 diff return
## edge 정보 저장 > 모든 edge 돌아가며, 끊었을 때마다 queue 하나를 새로 써서 두 set 의 node 숫자 차이를 계산하고, 최소값 리턴
#from collections import defaultdict, deque
#def solution(n, wires):
#    answer = 1000
#    edges = defaultdict(lambda:[])
#    new_wires = []
#    for s, d in wires:
#        new_wires.append([s-1,d-1])
#        
#    for s, d in new_wires:
#        edges[s] += [d]
#        edges[d] += [s]
#        
#    #print(edges)
#    for s, d in new_wires:
#        queue = deque([s]) # s 로 시작해야 모두 통과
#        visited = [0 for _ in range(n)]
#        while queue:
#            cur = queue.popleft()
#            if visited[cur] != 0:
#                continue
#            visited[cur] = 1
#            for next in edges[cur]:
#                if not (cur == s and next == d) or (cur == d and next == s): # 이 조건일때만 모두 통과, 의미는 s, d 를 끊었으니, s, d 를 통과하는 경로는 제외하자는 것
#                    queue.append(next)
#            #print(s, d, cur, queue)
#        #print(sum(visited))
#        diff = abs(n - (sum(visited) * 2))
#        answer = min(diff, answer)
#        
#    return answer

# 231219 Edge 별로 한쪽으로 DFS 하면서, 전체 갯수 - visited 가 가장 작은 edge 에서의 diff return
#from collections import defaultdict, deque
#def solution(n, wires):
#    answer = 1000
#    new_wires = []
#    edges = defaultdict(lambda:[])
#    for s, d in wires:
#        new_wires.append([s-1, d-1])
#    for s, d in new_wires:
#        edges[s] += [d]
#        edges[d] += [s]
#    for s, d in new_wires:
#        queue = deque([s])
#        visited = [0 for _ in range(n)]
#        while queue:
#            c = queue.popleft()
#            if visited[c] != 0:
#                continue
#            visited[c] = 1
#            for next in edges[c]:
#                if not ((c == s and next == d) or (next == s and c == d)):
#                    queue.append(next)
#        #print(s, d, sum(visited))
#        diff = abs(n - sum(visited)*2)
#        answer = min(answer, diff)
#        
#    return answer
