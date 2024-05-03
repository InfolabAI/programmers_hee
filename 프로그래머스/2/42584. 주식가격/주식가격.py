#def solution(prices):
#    return 0
#240313
from collections import deque
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i, p in enumerate(prices):
        while stack and stack[-1][1] > p:
            p_i, p_p = stack.pop()
            answer[p_i] = i - p_i
            #print(f"poped {p_i}, {p_p}")
        stack.append((i, p))
        #print(i, p, stack)
    
    for i, p in stack:
        answer[i] = len(prices) - i - 1
        
    #print(answer)
    
    return answer



















# 240312
#def solution(prices):
#    stack = []
#    answer = [0] * len(prices)
#    for i in range(len(prices)):
#        while stack != [] and stack[-1][1] > prices[i]: # NOTE 앞에가 틀리면 뒤에는 연산 안함
#            past, _ = stack.pop()
#            answer[past] = i - past # NOTE 여기서 몇 초 뒤에 떨어졌는지 이미 넣음.
#        stack.append([i, prices[i]])
#        print(answer, ">", stack)
#    for i, s in stack: # NOTE 안 떨어진 나머지는 뒤에서부터 자기 위치가 answer 이므로, 여기서 넣음.
#        answer[i] = len(prices) - 1 - i
#    return answer

#240312
#def solution(prices):
#    stack = []
#    answer = [0] * len(prices)
#    for i in range(len(prices)):
#        while stack and stack[-1][1] > prices[i]:
#            index, price = stack.pop()
#            answer[index] = i - index
#            #print(answer)
#        stack.append([i, prices[i]])
#    
#    for i, p in stack:
#        answer[i] = len(prices) - i - 1
#    
#    #print(answer)
#    return answer

