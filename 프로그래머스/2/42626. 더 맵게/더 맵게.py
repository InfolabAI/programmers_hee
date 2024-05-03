#def solution(scoville, K):
#    return
# 240326
import heapq
from heapq import heapify, heappush, heappop
def solution(scs, K):
    #help(heapq)
    heapify(scs)
    answer = 0
    while scs:
        sc = heappop(scs)
        if scs and sc < K:
            nsc = sc + heappop(scs)*2
            heappush(scs, nsc)
            answer += 1
            #print(f"push {nsc}")
        else:
            break
        #print(scs)
    if scs or sc >= K: # NOTE 틀린 부분. 마지막 1개를 pop 했는데 K 보다 클 경우를 생각해야 함.
        return answer
    else:
        return -1


















#from heapq import heapify, heappush, heappop
#def solution(scoville, K):
#    heapify(scoville)
#    for i in range(1000000):
#        #scoville의 길이는 2 이상 1,000,000 이하입니다.
#        try:
#            heappush(scoville, heappop(scoville)+(heappop(scoville)*2))
#            #모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return
#            if scoville[0] >= K: return i+1
#        except:
#            #모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
#            return -1







#from heapq import heapify, heappush, heappop
#def solution(scoville, K):
#    heapify(scoville)
#    ans = 0
#    while scoville:
#        if scoville[0] >= K:
#            break
#            
#        try:
#            heappush(scoville, heappop(scoville) + heappop(scoville)*2)
#        except:
#            return -1
#        
#        ans += 1
#        
#    return ans

