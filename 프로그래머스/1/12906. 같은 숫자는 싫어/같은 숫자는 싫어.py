#def solution(arr):
#    return
# 240326
def solution(arr):
    prev_c = None
    if len(arr) == 0:
        return []
    answer = []
    for i, c in enumerate(arr):
        if (c != prev_c and prev_c != None):
            answer.append(prev_c)
            
        if (i == len(arr) - 1):
            answer.append(c)
        prev_c = c
            
    return answer















#import numpy as np
#def solution(arr):
#    ret = [arr[0]]
#    for n in arr[1:]:
#        if n != ret[-1]:
#            ret += [n]
#        
#    return ret



#def solution(s):
#    # 함수를 완성하세요
#    a = []
#    for i in s:
#        if a[-1:] == [i]: continue
#        a.append(i)
#    return a

