#def solution(prs, lo):
#    return
# 240325
from collections import deque
def solution(prs, lo):
    q = deque([(p, l == lo) for l, p in enumerate(prs)])
    answer = 0
    while q:
        p, l = q.popleft()
        if any([np > p for np, nl in q]):
            q.append((p, l))
        else:
            answer += 1
            if l:
                break
        #print(p, l, q)
            
    return answer


















#def solution(priorities, location):
#    ans = 0
#    priorities_location = [ [p, 1] if i == location else [p, 0] for i, p in enumerate(priorities) ]
#    while priorities_location:
#        prlc = priorities_location.pop(0)
#        if any([prlc[0] < other[0] for other in priorities_location]):
#            priorities_location.append(prlc)
#        else:
#            ans += 1
#            if prlc[1] == 1:
#                return ans

#def solution(priorities, location):
#    queue = [(i, p) for i, p in enumerate(priorities)]
#    answer = 0
#    while queue:
#        # list pop 에서 중요한 것은? pop() 이 아니라, pop(0)
#        cur = queue.pop(0)
#        if any([cur[1] < q[1] for q in queue]):
#            queue.append(cur)
#        else:
#            answer += 1
#            if cur[0] == location:
#                return answer
#            

# 240322
#from collections import deque
#def solution(prs, lo):
#    q = deque([(pr, i == lo) for i, pr in enumerate(prs)])
#    num = 0
#    while q:
#        pr, is_t = q.popleft()
#        if any([pr < prq for prq, is_t_q in q]): # NOTE 틀린 부분. any 를 사용해서 모든 값에 대해 비교하는 것이 베스트.
#            q.append((pr, is_t))
#        else:
#            num += 1
#            if is_t:
#                break
#        #print(q, num)
#    
#    return num

