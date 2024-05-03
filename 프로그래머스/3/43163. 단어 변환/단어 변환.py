#def solution(begin, target, words):
#    return
# 240405
from collections import defaultdict
def distance(sw, tw):
    dist = 0
    for sc, tc in zip(sw, tw):
        if sc != tc:
            dist += 1
    return dist
        
def solution(begin, target, words):
    tmp = [begin] + words
    edges = defaultdict(list)
    for sw in tmp:
        for tw in tmp:
            if sw == tw:
                continue
            if distance(sw, tw) == 1:
                edges[sw] += [tw]
    
    stack = [begin]
    visited = []
    while stack:
        sw = stack.pop()
        visited.append(sw)
        if target in visited:
            return len(visited) - 1 # NOTE 틀린 부분. 이거 안 될 줄 알았는데 됨. 즉, DFS 는 특정 target 까지의 최단 거리를 맞출 수 있음
        for edge in edges[sw]:
            if edge not in visited:
                stack.append(edge)
        #print(stack, visited)
        
    return 0












# recursive DFS 버전(distance 함수 내부 포함 버전)
#def solution(begin, target, words):
#    if target not in words:
#        return 0
#
#    res = [float("inf")]
#
#    def dfs(s, w_list, d, visited):
#        if s == target:
#            res[0] = min(res[0], d)
#            return
#
#        for i in w_list:
#            unmatch = 0
#            for a, b in zip(s, i):
#                if a != b:
#                    unmatch += 1
#            if unmatch == 1 and (i not in visited):
#                t = d + 1
#                visited.add(i)
#                dfs(i, w_list, t, visited)
#                visited.remove(i) 
#
#    dfs(begin, words, 0, set())
#
#    return res[0]






# Distance 함수 및 stack DFS 버전
#def distance(a, b):
#    distance = 0
#    for el_a, el_b in zip(a, b):
#        if el_a != el_b:
#            distance += 1
#    return distance
#        
#from collections import defaultdict, deque
#def solution(begin, target, words):
#    edges = defaultdict(list)
#    visited = {}
#    words.append(begin)
#    for w1 in words:
#        visited[w1] = 0
#        for w2 in words:
#            if distance(w1, w2) == 1:
#                edges[w1].append(w2)
#
#    #print(edges)
#    def dfs(start):
#        stack = deque([start])
#        ans = 0
#        while stack:
#            w = stack.pop()
#            if w == target:
#                return ans
#            
#            if visited[w] == 0:
#                visited[w] = 1
#                ans += 1
#                
#            #print(w, edges[w], ans, visited)
#            for edge in edges[w]:
#                if visited[edge] == 0:
#                    stack.append(edge)
#        return 0
#                
#    return dfs(begin)            

# distance 함수 따로 표현 버전
#from collections import deque
#def distance(sw, tw):
#    distance = 0
#    for s, t in zip(sw, tw):
#        if s != t:
#            distance += 1
#    return distance
#        
#
#def solution(begin, target, words):
#    visited = {}
#    for w in words + [begin]:
#        visited[w] = 0
#    def dfs(start):
#        stack = deque([start])
#        count = 0
#        while stack:
#            cur_w = stack.pop()
#            if visited[cur_w] == 0:
#                visited[cur_w] = 1
#            for w in words:
#                if distance(w, cur_w) == 1 and visited[w] == 0:
#                    stack.append(w)
#            count += 1
#            if target in stack:
#                break
#        if target not in stack:
#            count = 0
#        return count
#    return dfs(begin)

