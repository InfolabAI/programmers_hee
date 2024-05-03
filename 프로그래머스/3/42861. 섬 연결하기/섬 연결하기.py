#def solution(n, costs):
#    return 0
# 240313
from collections import deque, defaultdict
from heapq import heapify, heappush, heappop
def solution(n, costs):
    answer = 0
    edges = defaultdict(list)
    for s, t, w in costs:
        edges[s].append( (w, t) )
        edges[t].append( (w, s) )
    cheap = []
    visited = [0] * n
    heappush(cheap, (0, 0) )
    while min(visited) == 0:
        w, s = heappop(cheap)
        if visited[s] == 1:
            continue
        visited[s] = 1 
        answer += w
        for nw, t in edges[s]:
            if visited[t] == 0:
                heappush(cheap, (nw, t) )
        
    return answer

















#import heapq as hq
#
#def solution(n, costs):
#    answer = 0
#    from_to = list(list() for _ in range(n))
#    visited = [False] * n
#    priority = []
#
#    for a, b, cost in costs:
#        from_to[a].append((b, cost))
#        from_to[b].append((a, cost))
#
#    hq.heappush(priority, (0, 0))
#    while False in visited: # heap 으로 가장 낮은 cost 부터 연결하되, 모든 점을 방문하면 stop 하여 최소 비용을 구함
#        cost, start = hq.heappop(priority)
#        if visited[start]: continue
#
#        visited[start] = True
#        answer += cost
#        for end, cost in from_to[start]:
#            if visited[end] : continue
#            else:
#                hq.heappush(priority, (cost, end))
#
#    return answer

# 240312
#from heapq import heapify, heappush, heappop
#from collections import defaultdict
#
#def solution(n, costs):
#    answer = 0
#    visited = [0] * n
#    edge = defaultdict(list)
#    for s, t, w in costs:
#        edge[s].append((w,t))
#        edge[t].append((w,s)) # NOTE 틀린부분. s --> t 뿐 아니라, t --> s 도 넣어줘야 함
#    costhp = []
#    heappush(costhp, (0,0)) # (w, s)
#    while min(visited) == 0:
#        w, s = heappop(costhp)
#        if visited[s]: # NOTE 틀린 부분. 이 if 문이 없어도 된다고 생각했음. s 가 이미 방문이면, answer 에 더하지 않도록 해야 함. 아래 visited 만으로는 충분하지 않은 이유는, node 1개에서 다음 node 들을 미리 추가하고 나서 방문하는 경우가 있기 때문. 그래서 이중으로 해줘야 함
#            continue
#        visited[s] = 1
#        answer += w
#        for nw, t in edge[s]:
#            if visited[t] == 0: # NOTE 차라리 여기 if 문은 없어도 됨. 그러나, 있으면 속도가 더 빨라짐
#                heappush(costhp, (nw, t))
#        print(costhp)
#    
#    return answer

