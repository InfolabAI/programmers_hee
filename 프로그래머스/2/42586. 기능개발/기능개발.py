#def solution(progresses, speeds):
#    return
# 240326.
import math
def solution(progresses, speeds):
    pre_rel = None
    pending = []
    answer = []
    for p, s in zip(progresses, speeds): 
        rel = math.ceil((100-p)/s)
        if pre_rel == None: # NOTE 틀린 부분. queue 쓸 필요 없이, pre_rel 을 넘으면 모두 배포하는 식으로 짜면 됨.
            pre_rel = rel
        #print(pre_rel, rel, end=' > ')
        if rel > pre_rel:
            pre_rel = rel
            answer.append(len(pending))
            pending = []
        pending.append(p)
        #print(pending, answer)
    answer.append(len(pending))
    #print(pending, answer)
    return answer



















#def solution(progresses, speeds):
#    Q=[]
#    for p, s in zip(progresses, speeds):
#        # days 계산할 때 헷갈렸음
#        days = (100-p)//s if (100-p)%s == 0 else (100-p)//s +1
#        print(days)
#        # 아래 조건식 계산할 때 헷갈렸음
#        if len(Q) == 0 or days>Q[-1][0]:
#            Q += [[days, 1]]
#        else:
#            Q[-1][1] += 1
#            
#    return [q[1] for q in Q]

# 참고
#def solution(progresses, speeds):
#    Q=[]
#    for p, s in zip(progresses, speeds):
#        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#            Q.append([-((p-100)//s),1])
#        else:
#            Q[-1][1]+=1
#    return [q[1] for q in Q]




#def solution(progresses, speeds):
#    from math import ceil
#    prev_release = 0
#    release_list = []
#    for p, s in zip(progresses, speeds):
#        release = ceil( (100-p)/s )
#        print(release)
#        if prev_release >= release:
#            release_list[-1] += 1
#        else:
#            release_list.append(1)
#            prev_release = release
#    return release_list
            
