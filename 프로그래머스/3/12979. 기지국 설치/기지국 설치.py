#def solution(n, stations, w):
#    return
# 240510
import math
def solution(n, stations, w):
    prev_s = 0
    empty_list = []
    for s in stations:
        mns, mxs = s-w, s+w
        empty_list.append(mns-prev_s-1)
        prev_s = mxs
        
    if n+1 - mxs-1 > 0:
        empty_list.append(n+1 - mxs-1)
        
    answer = 0
    for e in empty_list:
        answer += math.ceil(e/(w*2+1))
    
    return answer























#import math
#def solution(n, stations, w):
#    answer = 0
#    dist = []  # 전파 전달 안되는 구간 길이 저장할 리스트
#    for i in range(1, len(stations)):
#        dist.append((stations[i]-w-1)-(stations[i-1]+w))
#    
#    dist.append(stations[0]-w-1)  # 맨앞
#    dist.append(n-(stations[-1]+w))  # 맨뒤
#    
#    for i in dist:
#        if i <= 0:
#            continue
#        else:
#            answer += math.ceil(i/(2*w+1))  # 올림
#    return answer