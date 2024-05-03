#def solution(s):
#    return
# 240325
from collections import deque
def solution(s):
    if s[0] == ")":
        return False
    if len(set(s)) <= 1:
        return False
    q = deque([s[0]])
    for c in s[1:]:
        if c == "(":
            q.append(c)
        else:
            if not q: # NOTE 틀린 부분. 중간에 q 길이가 0 인데 ")))" 가 남을 수 있음
                return False
            q.pop()
    return len(q) == 0

































#from collections import deque
#def solution(s):
#    queue = deque()
#    for ch in s:
#        if ch == "(":
#            queue.append("(")
#        else:
#            if queue:
#                queue.popleft()
#            else:
#                return False
#    return False if queue else True

#from collections import deque
#def solution(s):
#    queue = deque()
#    for ss in s:
#        # 무엇을 append 하고 pop 할 것인가?
#        if ss == "(":
#            queue.append("(")
#        else:
#            try:
#                queue.popleft()
#            except:
#                return False
#    if len(queue) == 0:
#        return True
#    else:
#        return False

