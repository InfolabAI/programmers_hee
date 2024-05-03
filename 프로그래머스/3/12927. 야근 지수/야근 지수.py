import numpy as np
import heapq

def solution(n, works):
    answer = 0
    # 즉, n 만큼 works 의 모든 값이 같아지는 방향으로 변경한 후, 야근 지수 계산하면 정답.
    # n 에 따라, works 의 각 값은 min(works) 보다 작아질 수 있음.
    heapq.heapify(works := [-w for w in works])
    for i in range(n):
        heapq.heappush(works, min(heapq.heappop(works) + 1, 0))
    return sum([(w)**2 for w in works])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
## := 없는 버전
#import heapq
#
#def solution(n, works):
#    if n >= sum(works):
#        return 0
#    
#    works = [-w for w in works]
#    heapq.heapify(works)
#    for _ in range(n):
#        i = heapq.heappop(works)
#        i += 1
#        heapq.heappush(works, i)
#    
#    return sum([w ** 2 for w in works])
#        
#    return int(answer)
#
#
## := 있는 버전
#from heapq import heapify, heappush, heappop
#def solution(n, works):
#    heapify(works := [-i for i in works]) # NOTE 틀린 부분. 바다코끼리 연산자. 할당과 동시에 works 를 return 할 수 있음
#    for i in range(min(n, abs(sum(works)))):
#        heappush(works, heappop(works)+1)
#    return sum([i*i for i in works])
