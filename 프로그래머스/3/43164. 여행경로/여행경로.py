#from collections import defaultdict, deque
#def solution_sub(tickets):
#    return
# 240404 v2
from collections import defaultdict, deque
def solution_sub(tickets):
    edges = defaultdict(list)
    for s, t in tickets:
        edges[s] += [t]
    for s, ts in edges.items():
        edges[s] = sorted(ts, reverse=True)
    print(edges)
    stack = ["ICN"]
    visited = []
    while stack:
        # 한 번 방문한 곳을 다시 방문해야 함 AND 중간에 끊기면 안됨, 즉, 정답에 넣는 것은 더이상 방문할 곳이 없을때만 넣음.
        s = stack[-1]
        if len(edges[s]) == 0:
            visited.append(stack.pop())
        else:
            stack.append(edges[s].pop())
    return visited[::-1]

def solution(tickets):
    # 테케 1, 2 통과를 위한 예제
    #tickets = [["ICN", "D"], ["D", "ICN"], ["ICN", "B"]]
    #answer = ['ICN', 'D', 'ICN', 'B'] 
    return solution_sub(tickets)

	




















#from collections import defaultdict
#def solution_sub(tickets):
#    routes = defaultdict(list)
#    # 공항 t[0] 에서 갈수 있는 모든 공항을 담음
#    # e.g., {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}
#    for t in tickets:
#        routes[t[0]] = routes[t[0]] + [t[1]]
#        
#    # 공항 t[0] 에서 갈수 있는 모든 공항을 내림차순 sort 함
#    # e.g., {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['SFO', 'ICN']}
#    for r in routes:
#        routes[r].sort()
#        
#    stack = ["ICN"]
#    path = []
#    # DFS
#    while len(stack) > 0:
#        # pop 이 아니라 top 을 봄
#        top = stack[-1]
#        # 즉, 시작공항이 아니거나 or 시작공항이어도 갈수있는 공항이 없으면
#        if top not in routes or len(routes[top]) == 0:
#            path.append(stack.pop())
#        else:
#            # 즉, 시작공항이고 갈수있는 공항이 있으면
#            stack.append(routes[top].pop(0)) # 가장 첫 공항을 빼서 스택에 넣음
#    return path[::-1]

# 240404
#from collections import defaultdict, deque
#def solution_sub(tickets):
#    edges = defaultdict(list)
#    for s, d in tickets:
#        edges[s] += [d]
#    for s, ds in edges.items():
#    	edges[s] = sorted(ds, reverse=True) # NOTE 틀린 부분. stack 은 나중에 넣은게 먼저 나오므로, 큰 알파벳부터.
#    """
#    tickets == 	[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
#    일때,
#    edges == {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['SFO', 'ICN']})
#    """
#    visited = []
#    stack = ["ICN"]
#   	 
#    while stack:
#        """
#        s = stack.pop()
#        for d in edges[s]: # NOTE 틀린 부분. 이렇게 하면 A > B , A > C 만 티켓이 있어도 A > B > C 를 가는 상황이 생김. 즉, B > C 는 ticket 이 없는데 있는 것처럼 처리됨.
#            stack.append(d)
#        """
#        s = stack[-1] # NOTE 틀린 부분. 다음에 갈 수 있는 공항이 없는 공항은 마지막까지 방문을 보류해야 함. 그래서 pop() 이 하닌 stack[-1] 을 보는 것.
#        if len(edges[s]) == 0:
#            visited.append(stack.pop())
#        else:
#            stack.append(edges[s].pop())
#        #print(s, stack)
#    	
#    return visited[::-1] # NOTE 틀린 부분. stack 이라서 ICN 이 맨 마지막에 추가되므로, 거꾸로 해야 함

