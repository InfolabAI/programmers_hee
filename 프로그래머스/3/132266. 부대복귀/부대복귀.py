def solution(n, roads, sources, destination):
    return

# 240813 BFS 인데 역으로 destination 에서 모든 source 까지의 거리를 저장하고 사용한다면?
from collections import defaultdict, deque
def bfs(st, edges, n):
    D = [-1 for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    queue = deque([[st, 0]])
    visit[st] = 1
    while queue:
        cur, dist = queue.popleft()
        D[cur] = dist
        for nt in edges[cur]:
            if visit[nt] == 0:
                queue.append([nt, dist+1])
                visit[nt] = 1
    return D
            
def solution(n, roads, sources, destination):
    answer = []
    edges = defaultdict(list)
    for s, d in roads:
        edges[s] += [d]
        edges[d] += [s]
    
    #bfs(1, edges, destination, n)
    D = bfs(destination, edges, n)
    return [D[s] for s in sources]

# 240813 NOTE 틀린 부분. BFS 로 푼다면? 정답이지만, 시간 초과가 발생함
#from collections import defaultdict, deque
#def bfs(st, edges, dt, n):
#    visit = [0 for _ in range(n+1)]
#    queue = deque([[st, 0]])
#    while queue:
#        cur, dist = queue.popleft()
#        if cur == dt:
#            return dist
#        for nt in edges[cur]:
#            if visit[nt] == 0:
#                queue.append([nt, dist+1])
#                visit[nt] = 1
#    return -1
#            
#def solution(n, roads, sources, destination):
#    answer = []
#    edges = defaultdict(list)
#    for s, d in roads:
#        edges[s] += [d]
#        edges[d] += [s]
#    
#    #bfs(1, edges, destination, n)
#    return [bfs(s, edges, destination, n) for s in sources]

# ref https://velog.io/@mrbartrns/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B6%80%EB%8C%80-%EB%B3%B5%EA%B7%80python
#import heapq
#
#INF = 987654321
#def dijkstra(start, adj, distance):
#    q = []
#    distance[start] = 0
#    heapq.heappush(q, (0, start))
#
#    while q:
#        dist, node = heapq.heappop(q)
#
#        # 메모된 거리가 dist보다 짧다면 더 이상 탐색할 필요가 없다.
#        if distance[node] < dist:
#            continue
#
#        for nxt in adj[node]:
#            nxt_distance = dist + 1
#
#            if distance[nxt] > nxt_distance:
#                distance[nxt] = nxt_distance
#                heapq.heappush(q, (nxt_distance, nxt))
#
#def solution(n, roads, sources, destination):
#    adj = [[] for _ in range(n + 1)]
#    distance = [INF] * (n + 1)
#    answer = []
#
#    # create graph
#    for a, b in roads:
#        adj[a].append(b)
#        adj[b].append(a)
#
#    # get distance array
#    dijkstra(destination, adj, distance)
#
#    # return value by sources
#    for source in sources:
#        value = distance[source]
#        answer.append(value if value < INF else -1)
#
#    return answer