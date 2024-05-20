from collections import defaultdict
def match(stra, strb):
    i = 0
    if len(stra) != len(strb):
        return False
    for a, b in zip(stra, strb):
        if b != "*" and a != b:
            return False
    return True

def solution(user_id, banned_id):
    # NOTE 틀린 부분.
    # 1. 하나의 user_id 가 다수의 banned_id 에 걸린다면 어떻게 처리하는가? 예를 들어, frodo 가 'fr*d*' 에도 골리고, '*rodo' 에도 걸린다면?
    # 2. 중복된 banned_id 는 어떻게 처리하는가?
    # DFS 로 처리하면 해결되는데, 무엇이 edge, node 인가?
    answer = 0
    matched_dict = defaultdict(list) 
    for uid in user_id:
        for bid in banned_id:
            if match(uid, bid):
                matched_dict[bid].append(uid)
    
    print(matched_dict)
    return answer

# ref2 테케5 에서 9000ms 걸림. 엄청 느림
#from itertools import product
#
#def check(str1, str2):
#    if len(str1) != len(str2):
#        return False
#    for i in range(len(str1)):
#        if str1[i] == "*":
#            continue
#        if str1[i] != str2[i]:
#            return False
#    return True
#
#def solution(user_id, banned_id):
#    answer = set()
#    result = [[] for i in range(len(banned_id))]
#
#    for i in range(len(banned_id)):
#        for u in user_id:
#            if check(banned_id[i], u):
#                result[i].append(u)
#
#    result = list(product(*result))
#    for r in result:
#        if len(set(r)) == len(banned_id):
#            answer.add("".join(sorted(set(r))))
#
#    return len(answer)

# ref 테케5 에서 90ms 걸림. 빠름 (비트 연산은 길이에 제한적으로 사용가능한 방법이기에 제외)
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
#        # bs 는 ckeck (dict)에 사용할 key
#        # check 는 True 가 담기는 dict
#        if check.get(bs)!=None: return 0
#        check[bs]=True
#        return 1
#    
#    cnt = 0
#    # dep 마다, banned_id 하나에 해당하는 계산을 진행함
#    # 입력 ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"] 일때
#    # candidate_id == 	[[0, 1], [3]] 이고
#    # dep 마다 [0,1] , [3] 에 대해 cnt 계산 진행하고, [3] 에 대한 cnt (return 1) 가 [0,1] 에 대한 cnt 에 이용됨
#    # 중복 여부를 bitmasking으로 구현
#    for id in candidate_id[dep]:
#        print('bs', bin(bs), bin(1), bin(id), bin(1<<id))
#        print(bs, id, 1<<id, bs&(1<<id), bs^(1<<id))
#        if bs&(1<<id)!=0: continue
#        
#        bs=bs^(1<<id)
#        cnt += combination(candidate_id, dep+1, bs, check)
#        bs=bs^(1<<id)
#    
#    print(bs, check)
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
#    # 입력 ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"] 일때
#    # candidate_id == 	[[0, 1], [3]]
#    print(candidate_id)
#    return combination(candidate_id, 0, 0, dict())

# ref 3
def solution(user_id, banned_id):
    answer = set()
    ban_length = len(banned_id)
    user_length = len(user_id)
    #벤길이과 유저길이가 같다면 경우의 수는 1개라고 리턴
    if ban_length == user_length:
        return 1
    #걸린 유저 체크용
    use_user = [1 for _ in range(user_length)]
    #사용된 벤유저 체크용
    use_ban = [1 for _ in range(ban_length)]
    #dfs를 이용하여 경우의 수를 검사
    stack = []
    #첫 시작은 0부터이다.
    stack.append([0, use_user, use_ban])
    #스택이 빌때까지 반복
    while stack:
        #스택에서 데이터를 꺼내 매칭
        idx, use_user, use_ban = stack.pop()
        #모든 벤유저를 찾았다면 정답에 추가
        #중복을 방지하기 위해 셋구조에 추가
        if idx == ban_length:
            temp = []
            for i in range(user_length):
                if not use_user[i]: temp.append(user_id[i])
            if temp: answer.add(tuple(temp))
        #벤유저와 모든 유저를 반복해서 돈다.
        for i in range(ban_length):
            #체크한 벤유저가 아니라면
            if use_ban[i] : 
                for j in range(user_length):
                    # 사용한 유저가 아니어야 하고, 벤유저아이디 길어와 유저아이디 길이가 같아야 한다.
                    if use_user[j] and len(banned_id[i]) == len(user_id[j]):
                        #반복문을 돌면서 둘이 매칭되는지 확인한다. * 인경우 넘어간다.
                        for k in range(len(user_id[j])):
                            if user_id[j][k] != banned_id[i][k] and banned_id[i][k] != '*':
                                break
                        #break가 걸리지 않았다면
                        else:
                            #유저와 벤유저 모드 체크하고
                            use_user[j] = 0
                            use_ban[i] = 0
                            #스택에 추가한다.
                            stack.append([idx+1, use_user[:], use_ban[:]])
                            #체크한것을 해제
                            use_user[j] = 1
                            use_ban[i] = 1
    #set의 길이가 경우의 수이다.
    return len(answer)