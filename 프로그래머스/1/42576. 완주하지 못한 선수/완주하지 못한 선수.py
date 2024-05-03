#def solution(participant, completion):
#    return
# 240322
from collections import Counter
def solution(participant, completion):
    ret = Counter(participant) - Counter(completion)
    return list(ret.keys())[0]



















##### Counter 를 이용
#def solution(participant, completion):
#    import collections
#    
#    ct = collections.Counter(participant) - collections.Counter(completion)
#    print(ct)
#    # ct.keys() 에 [0] 가 먹히지 않을때 어떻게 해야 합니까?
#    return list(ct.keys())[0]
    
    
#####sort 해서 위치별 비교
#def solution(participant, completion):
#    participant.sort()
#    completion.sort()
#    
#    # 더 긴 list 까지 진행하는 방법은?
#    from itertools import zip_longest
#    for p, c in zip_longest(participant, completion):
#        if p != c:
#            return p
        
##### hash 값의 가감으로 찾음
#def solution(participant, completion):
#    p_dict = {}
#    tmp = 0
#    # hash 값이 무엇이든, 더하고 빼기 후엔 정확히 return 한명의 hash 값만 남는다.
#    for p in participant:
#        p_dict[hash(p)] = p
#        tmp += hash(p)
#    for c in completion:
#        tmp -= hash(c)
#    return p_dict[tmp]

