#def solution(n, stations, w):
#    return

# 240910
def solution(n, stations, w):
    prev = 0
    blocks = []
    stations += [n+w+1]
    for st in stations: # 빈 공간들의 크기만 저장하고
        st = st-1
        tmp = st-w-prev
        if tmp > 0:
            blocks.append(tmp)
        prev = st+w+1
        #print(st, tmp, prev)
        
    answer = 0
    for bl in blocks: # 몇 개의 기지국으로 채울 수 있는지 저장
        answer += bl // (w*2+1)
        if bl % (w*2+1) > 0:
            answer += 1
    return answer





# 240510
#import math
#def solution(n, stations, w):
#    prev_s = 0
#    empty_list = []
#    for s in stations: # 빈공간 계산
#        mns, mxs = s-w, s+w
#        empty_list.append(mns-prev_s-1)
#        prev_s = mxs
#        
#    if n+1 - mxs-1 > 0: # 끝과의 빈공간 추가
#        empty_list.append(n+1 - mxs-1)
#        
#    answer = 0
#    for e in empty_list: # 빈 공간마다 필요한 기지국 수 계산
#        answer += math.ceil(e/(w*2+1))
#    
#    return answer













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