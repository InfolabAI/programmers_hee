#def solution(n, vertex):
#    return
# 240419
from collections import deque, defaultdict
def solution(n, vertex):
    edges = defaultdict(list)
    for s, t in vertex:
        s, t = s, t
        edges[s] += [t]
        edges[t] += [s]
    visited = [0] * (n+1)
    
    queue = deque([(1, 0)])
    visited[1] = 1
    total = []
    while queue:
        s, dist = queue.popleft()
        for t in edges[s]:
            if visited[t] == 0:
                queue.append((t, dist+1))
                total.append(queue[-1])
                visited[t] = 1
        #print(queue)
    
    max_dist = max([x[1] for x in total])
    answer = 0
    for i, dist in total:
        if dist == max_dist:
            answer += 1
        
    return answer








#from collections import deque
#def solution(n, vertex):
#    # edges: 중복없는 edge 를 담는 자료구조(e.g., [[2, 1], [2, 0, 3, 4], [5, 3, 1, 0], [2, 1], [1], [2], []])
#    edges = [[] for _ in range(n)]
#    # 1에서부터의 최소 거리만 있으면 되니까 점마다 distance 1개인데, 모두 0임. 1에서부터의 간선이 직접 연결 외에는 없고, 모든 edge weight가 1이기 때문.
#    distance = [0 for _ in range(n)]
#    visited = [0 for _ in range(n)]
#    for s, t in vertex:
#        edges[s-1] += [t-1]
#        edges[t-1] += [s-1]
#    
#    queue = deque([0])
#    # 만약 간선마다 weight 가 다르면, 여기서 queue 가 아니라 heapq 를 써야함. https://jaemunbro.medium.com/algorithm-%EC%B5%9C%EB%8B%A8-%EA%B2%BD%EB%A1%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-with-python-20f061fdc8f1
#    while queue:
#        cur = queue.popleft()
#        if visited[cur] == 0:
#            visited[cur] = 1
#        for n in edges[cur]:
#            if visited[n] == 0:
#                visited[n] = 1
#                # dynamic programming 처럼 1에서부터의 원래 거리와 중첩계산되어 온 방문한 노드의 distance 중 짧은 거리를 넣으면 되는데, 여기선 1에서 직접 연결된 다른 간선이 없다고 간주하기 때문에 그냥 1 더하는 것으로 끝.
#                distance[n] = distance[cur] + 1
#                queue.append(n)
#    #가장 먼 distance가 몇개인지 세어야 함.
#    return distance.count(max(distance))


#from collections import deque
#def solution(n, vertex):
#    edges = [[] for _ in range(n)]
#    distance = [0 for _ in range(n)]
#    visited = [0 for _ in range(n)]
#    for s, t in vertex:
#        edges[s-1] += [t-1]
#        edges[t-1] += [s-1]
#    
#    q = deque([0])
#    
#    while q:
#        k = q.popleft()
#        
#        if visited[k] == 0:
#            visited[k] = 1
#            
#        for i in edges[k]:
#            if visited[i] == 0:
#                visited[i] = 1
#                distance[i] = distance[k] + 1
#                q.append(i)
#                
#    return distance.count(max(distance))

