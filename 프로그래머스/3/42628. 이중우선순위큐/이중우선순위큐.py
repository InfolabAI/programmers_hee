#def solution(operations):
#    return
# 240202
import heapq as hq
def solution(operations):
    ret = []
    
    for operation in operations:
        op, num = operation.split(" ")
        if op == "I":
            hq.heappush(ret, int(num))
        else:
            if num[0] > "-":
                ret = sorted(ret, reverse=True)[1:]
                hq.heapify(ret)
            else:
                #hq.heappop(ret) # NOTE 틀린부분
                ret = ret[1:]    # 이렇게 하면 테케 2,4번 에러가 안남
                hq.heapify(ret)
        #print(ret)
        
    if len(ret) == 0:
        return [0, 0]
    else:
        #return [hq.nlargest(1, ret)[0], hq.nsmallest(1, ret)[0]]
        return [max(ret), min(ret)]




















#import heapq
##https://think-tech.tistory.com/69
#def solution(operations):
#    heap = []
#    for operation in operations :
#        op0, op1 = operation.split()
#        if op0 == "I" :
#            heapq.heappush(heap, int(op1))
#        elif heap :
#            if op1 == "1" : # 최댓값 삭제
#                heap = heapq.nlargest(len(heap), heap)[1:]
#                heapq.heapify(heap)
#            elif op1 == "-1" :
#                heapq.heappop(heap)
#    
#    if heap :
#        min_value = heapq.heappop(heap)
#        if heap :
#            max_value = heapq.nlargest(1, heap)[0]
#        else : 
#            max_value = min_value
#    else :
#        max_value, min_value = 0, 0
#    
#    return [max_value, min_value]

# 231208
#from heapq import nlargest, heapify, heappush
#def solution(operations):
#    heap = []
#    for operation in operations:
#        op, num = operation.split(" ")
#        num = int(num)
#        if op == "I":
#            heappush(heap, num)
#        else:
#            if num < 0:
#                heap = heap[1:]
#            else:
#                heap = nlargest(len(heap), heap)[1:]
#                heapify(heap)
#                
#    if len(heap) == 0:
#        return [0,0]
#    else:
#        return [max(heap), min(heap)]
