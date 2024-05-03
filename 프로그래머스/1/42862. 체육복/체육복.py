#def solution(n, lost, reserve):
#    return
# 240328
def lend_after(i, cl, n):
    if i != n-1:
        if cl[i] == cl[i+1] + 2:
            cl[i] -= 1
            cl[i+1] +=1
            
def lend_before(i, cl, n):
    if i != 0:
        if cl[i] == cl[i-1] + 2:
            cl[i] -= 1
            cl[i-1] +=1
            
import numpy as np
def solution(n, lost, reserve):
    lost = list(map(lambda x:x-1, lost))
    reserve = list(map(lambda x:x-1, reserve))
    cl = [1] * n
    cl = [x-1 if i in lost else x for i, x in enumerate(cl)]
    cl = [x+1 if i in reserve else x for i, x in enumerate(cl)]
    
    #print(cl)
    for i, s in enumerate(cl):
        lend_before(i, cl, n)
        lend_after(i, cl, n)
    
    return len(np.array(cl).nonzero()[0])





















#from collections import Counter
#def solution(n, lost, reserve):
#    # lost와 reserve 가 정렬되어 있다고 가정하면 안됨
#    lost.sort()
#    reserve.sort()
#    
#    # 도난당한 학생중에 여벌 체육복 가져온 학생 제외
#    lost_ = sorted(Counter(lost) - Counter(reserve))
#    # 여벌 체육복을 가져온 학생 중에 도난당한 학생 제외
#    reserve_ = sorted(Counter(reserve) - Counter(lost))
#    
#    # 도난 안 당한 여벌 체육복 가져온 학생이 빌려줄 수 있는 도난당한 학생 제거
#    for r in _reserve:
#        f = r - 1
#        b = r + 1
#        if f in _lost:
#            _lost.remove(f)
#        elif b in _lost:
#            _lost.remove(b)
#    return n - len(_lost)


#from collections import Counter
#def solution(n, lost, reserve):
#    lost.sort()
#    reserve.sort()
#    lost_new = list(Counter(lost) - Counter(reserve))
#    reserve_new = list(Counter(reserve) - Counter(lost))
#
#    still_lost = []
#    for i in lost_new:
#        if i-1 in reserve_new:
#            reserve_new.remove(i-1)
#        elif i+1 in reserve_new:
#            reserve_new.remove(i+1)
#        else:
#            still_lost += [i]
#    return n - len(still_lost)


