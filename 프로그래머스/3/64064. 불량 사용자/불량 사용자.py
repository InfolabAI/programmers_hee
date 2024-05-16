def solution(user_id, banned_id):
    answer = 0
    return answer

# ref2
from itertools import product

def check(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] == "*":
            continue
        if str1[i] != str2[i]:
            return False
    return True

def solution(user_id, banned_id):
    answer = set()
    result = [[] for i in range(len(banned_id))]

    for i in range(len(banned_id)):
        for u in user_id:
            if check(banned_id[i], u):
                result[i].append(u)

    result = list(product(*result))
    for r in result:
        if len(set(r)) == len(banned_id):
            answer.add("".join(sorted(set(r))))

    return len(answer)

# ref
#def match(id, ban):
#    if len(id)!=len(ban):
#        return False
#    
#    for i in range(len(id)):
#        if ban[i]!='*' and ban[i]!=id[i]:
#            return False
#    return True
#
#def combination(candidate_id, dep, bs, check):
#    if dep>=len(candidate_id):
#        if check.get(bs)!=None: return 0
#        check[bs]=True
#        return 1
#    
#    cnt = 0
#    for id in candidate_id[dep]:
#        if bs&(1<<id)!=0: continue
#        
#        bs=bs^(1<<id)
#        cnt += combination(candidate_id, dep+1, bs, check)
#        bs=bs^(1<<id)
#    
#    return cnt
#    
#
#def solution(user_id, banned_id):
#    answer = 0
#    candidate_id = []
#    
#    for ban in banned_id:
#        candidate_id.append([])
#        for i in range(len(user_id)):
#            if match(user_id[i], ban):
#                candidate_id[-1].append(i)
#        
#    return combination(candidate_id, 0, 0, dict())