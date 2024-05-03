#def solution(clothes):
#    return 0
# 240207
from collections import defaultdict
import numpy as np
def solution(clothes):
    type_dict = defaultdict(list)
    for n, t in clothes:
        type_dict[t] += [n]
    
    return int(np.array([len(list_)+1 for t, list_ in type_dict.items()]).prod() -1)












# defaultdict 버전
#from collections import defaultdict
#def solution(clothes):
#    answer = 1
#    hashmap = defaultdict(lambda:1)
#    print(clothes)
#    for name, type in clothes:
#        hashmap[type] += 1
#    for type, num in hashmap.items():
#        answer *= num
#    return answer-1


#def solution(clothes):
#    # 1. 옷을 종류별로 구분하기
#    hash_map = {}
#    for clothe, type in clothes:
#        hash_map[type] = hash_map.get(type, 0) + 1
#        
#    # 2. 입지 않는 경우를 추가하여 모든 조합 계산하기
#    answer = 1
#    for type in hash_map:   
#        answer *= (hash_map[type] + 1)
#    
#    # 3. 아무종류의 옷도 입지 않는 경우 제외하기
#    return answer - 1

# 231215
#from collections import defaultdict
#def solution(clothes):
#    answer = 1
#    hashmap = defaultdict(lambda:1)
#    for name, type in clothes:
#        hashmap[type] += 1
#    for type, num in hashmap.items():
#        answer *= num
#    return answer - 1

