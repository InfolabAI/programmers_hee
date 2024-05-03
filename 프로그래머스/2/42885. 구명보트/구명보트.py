#def solution(pp, limit) :
#    return
# 240318
def solution(pp, limit) :
    pp = sorted(pp, key=lambda x:x, reverse=True)
    diff = 0
    i, j = 0, len(pp) - 1
    while i < j:
        #print(pp[i], pp[j])
        if pp[i] + pp[j] <= limit:
            diff += 1
            i += 1
            j -= 1
        else: # NOTE 틀린 부분. else 를 빼먹었었는데, 위 조건이 아닐때만 i 를 늘려야 함. else 없으면 i 는 2씩 늘어나기 때문.
            i += 1
        #print(diff)
    
    return len(pp) - diff








#def solution(people, limit) :
#    answer = 0
#    people.sort()
#
#    a = 0
#    b = len(people) - 1
#    while a < b :
#        # 한번에 최대 2명이라서 이 조건이면 됨
#        if people[b] + people[a] <= limit :
#            a += 1
#            # 두명을 옮길 수 있으면, 필요한 구명보트 수가 1개 줄어듬.
#            answer += 1
#            #print(f'{a, people[a], b, people[b]}')
#        b -= 1
#    # worst 는 모든 사람을 1번에 1명씩 옮긴 것. 즉, len(people).
#    return len(people) - answer

#def solution(people, limit):
#    from collections import deque
#    people.sort()
#    p_q = deque(people)
#    
#    ans = len(people)
#    while p_q:
#        if len(p_q) >= 2: 
#            left, right = p_q.popleft(), p_q.pop()
#            if (left+right) <= limit:
#                ans -= 1
#            else:
#                p_q.appendleft(left)
#        else:
#            weight = p_q.popleft()
#            
#    return ans

#def solution(people, limit) :
#    answer = 0
#    people.sort()
#    a = 0
#    b = len(people) - 1
#    while a < b:
#        if people[a] + people[b] <= limit:
#            a += 1
#            answer += 1
#        
#       	b -= 1 
#            
#    return len(people) - answer

# 240314
#def solution(people, limit) :
#    people = sorted(people, key=lambda x:x, reverse=True)
#    #print(people)
#    answer = 0
#    i, j = 0, len(people) - 1
#    while people and i < j:
#        if people[i] + people[j] <= limit:
#            #del people[j] # NOTE 틀린 부분. 굳이 삭제하지 말고, 둘이 탈 수 있는 횟수를 총 사람 수에서 빼는 쪽으로 진행하는 것이 효율성이 좋음.
#            #del people[i]
#            j -= 1
#            i += 1
#            answer += 1
#            #print(f"DEL {i}, {j}")
#        else:
#            i += 1
#    
#    return len(people) - answer

# 240315
#def solution(people, limit) :
#    people = sorted(people, key=lambda x:x, reverse=True)
#    i, j = 0, len(people)-1
#    num_two = 0
#    while i < j:
#        if people[i] + people[j] <= limit:
#            i += 1
#            j -= 1
#            num_two += 1
#        else:
#            i+=1
#    return len(people) - num_two



