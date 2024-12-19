def solution(gems):
    answer = []
    return answer

## 241219-3  # st, ed 를 움직여가며 수행해서 훨씬 빨라졌고 답도 맞으나, 효율성은 시간 초과. dict 를 써서 중복 체크를 더 빠르게 했지만, 효율성 테스트 중 일부를 통과 못함
from collections import defaultdict
def get_set_len(gems_dict):
    len_ = 0
    for k in gems_dict:
        if gems_dict[k] > 0:
            len_ += 1
    return len_
        
# 241219 candidate sorting 을 없애도록 효율화 했으나, 그래도 효율성 테스트 통과 못함
def solution(gems):
    answer = []
    st, ed = 0, 0
    max_len = len(set(gems))
    gems_dict = defaultdict(lambda:0)
    gems_dict[gems[0]] += 1
    min_cand_len = 100000
    
    do_ = True
    i = 0
    while do_:
        if len(gems_dict) == max_len and st <= ed:
            st += 1
            gems_dict[gems[st-1]] -= 1
            if gems_dict[gems[st-1]] <= 0:
                del gems_dict[gems[st-1]]
            if ed - st < min_cand_len:
                candidate = (st, ed)
                min_cand_len = ed - st
        else:
            ed += 1
            if ed >= len(gems):
                break
            gems_dict[gems[ed]] += 1
            
        
    #print(candidate)
    #candidate = sorted(candidate, key=lambda x:x[1]-x[0])
    return [candidate[0], candidate[1]+1]

## 241219-2  # st, ed 를 움직여가며 수행해서 훨씬 빨라졌고 답도 맞으나, 효율성은 시간 초과. dict 를 써서 중복 체크를 더 빠르게 했지만, 효율성 테스트 중 일부를 통과 못함
#from collections import defaultdict
#def get_set_len(gems_dict):
#    len_ = 0
#    for k in gems_dict:
#        if gems_dict[k] > 0:
#            len_ += 1
#    return len_
#        
#def solution(gems):
#    answer = []
#    st, ed = 0, 0
#    max_len = len(set(gems))
#    candidate = []
#    gems_dict = defaultdict(lambda:0)
#    gems_dict[gems[0]] += 1
#    
#    do_ = True
#    i = 0
#    while do_:
#        if get_set_len(gems_dict) == max_len and st <= ed:
#            st += 1
#            gems_dict[gems[st-1]] -= 1
#            candidate.append((st, ed))
#        else:
#            ed += 1
#            if ed >= len(gems):
#                break
#            gems_dict[gems[ed]] += 1
#            
#        
#    #print(candidate)
#    candidate = sorted(candidate, key=lambda x:x[1]-x[0])
#    return [candidate[0][0], candidate[0][1]+1]

## 241219  # st, ed 를 움직여가며 수행해서 훨씬 빨라졌으나, 효율성은 시간 초과
"""
- 출발점, 종점 둘 다 0 부터 시작해서 가장 처음으로 모든 보석이 모이는 종점을 찾고, 그 종점을 기준으로 출발점을 키워 간다. 출발점을 키워 가다, 보석이 전부 모이지 않는 경우가 발생하면 종점을 다시 늘린다.
- 이걸 반복하다 종점이 최대 크기에 도달하면 반복을 중단한다.
- 그렇게 모인 구간들의 집합에서 거리가 가장 짧은 것을 구한다. 구간들은 순서대로 들어있기 때문에, 따로 정렬을 해줄 필요는 없다.
"""
#def solution(gems):
#    answer = []
#    st, ed = 0, 0
#    max_len = len(set(gems))
#    candidate = []
#    while True:
#        #print(st, ed)
#        if len(set(gems[st:ed])) == max_len:
#            st += 1
#            candidate.append((st, ed))
#        else:
#            ed += 1
#            if ed == len(gems) + 1:
#                break
#        
#    candidate = sorted(candidate, key=lambda x:x[1]-x[0])
#    return candidate[0]

## 241213 # bfs 재귀로 풀면 정답은 맞는데 효율성을 통과하지 못함
#from collections import defaultdict, deque
#def bfs(depth, cur_gems, gemN, i, j):
#    rets = []
#    #print(depth, cur_gems[i:j], i, j)
#    for k in range(2):
#        if k == 0:
#            tmpj = j-1
#            if len(set(cur_gems[i-1:tmpj])) == gemN and i <= tmpj:# and depth < 5:
#                right = bfs(depth+1, cur_gems, gemN, i, tmpj)
#            else:
#                right = (depth, i, j)
#        else:
#            tmpi = i+1
#            if len(set(cur_gems[tmpi-1:j])) == gemN and tmpi <= j:# and depth < 5:
#                left = bfs(depth+1, cur_gems, gemN, tmpi, j)
#            else:
#                left = (depth, i, j)
#    ij = sorted([left, right], key=lambda x:x[0])[-1]
#    return ij
#    
#def solution(gems):
#    #print(gems)
#    ret= bfs(0, gems, len(set(gems)), 1, len(gems))
#    return [ret[1], ret[2]]


# 240605
#from collections import defaultdict
#from heapq import heappush
#def gems_to_dict(gems, dict_):
#    for gem in gems:
#        dict_[gem] += 1
#        
#def solution(gems):
#    answers = []
#    all_gems = defaultdict(int)
#    gems_to_dict(gems, all_gems)
#    i, j = 0, 0
#    #print(all_gems)
#    cur_gems = defaultdict(int)
#    cur_gems[gems[0]] += 1
#    if len(all_gems.keys()) == 1:
#        return [1,1]
#    #print(sum([v for k, v in all_gems.items()]))
#    while i<=j and j < len(gems):
#        #print(i, j, cur_gems)
#        if len(cur_gems) != len(all_gems): # NOTE 틀린 부분. 원래 두 dict 의 keys() 끼리 비교하는 구문이었고, 이 때 효율설 13, 15 통과 못했는데, len(dict) 를 비교하니 통과됨
#            #print("j++ ", end='')
#            if i > 0:
#                # heap 기준(길이), i 위치, j 위치 를 넣음
#                heappush(answers, [j-(i-1), i-1,j]) # NOTE 틀린 부분. append 시점 1. j 가 찾아진 후, i 를 늘리며 좁히다가 다시 j 를 늘릴 때
#            j += 1
#            if j != len(gems):
#                cur_gems[gems[j]] += 1
#        else:
#            #print("i++ ", end='')
#            cur_gems[gems[i]] -= 1
#            if cur_gems[gems[i]] <= 0:
#                del cur_gems[gems[i]]
#            i += 1
#            
#    #print(answers)
#    if len(answers) == 0:
#        return [1, len(gems)] # NOTE 틀린 부분. append 시점 2. j 가 찾아진 후, i 를 늘리는 상황이 한 번도 없을 때
#    
#    # NOTE 틀린 부분. 빠르게 만들기 위해 마지막에 sort 를 제외하고 heap 으로 처리했는데도 틀림.
#    a1, a2 = answers[0][1]+1, answers[0][2]+1
#    #print(answers)
#    return [a1, a2]


# ref (https://velog.io/@qkre/%EC%B9%B4%EC%B9%B4%EC%98%A4-Python-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%B8%ED%84%B4%EC%8B%AD-%EB%B3%B4%EC%84%9D-%EC%87%BC%ED%95%91)
"""
- 출발점, 종점 둘 다 0 부터 시작해서 가장 처음으로 모든 보석이 모이는 종점을 찾고, 그 종점을 기준으로 출발점을 키워 간다. 출발점을 키워 가다, 보석이 전부 모이지 않는 경우가 발생하면 종점을 다시 늘린다.
- 이걸 반복하다 종점이 최대 크기에 도달하면 반복을 중단한다.
- 그렇게 모인 구간들의 집합에서 거리가 가장 짧은 것을 구한다. 구간들은 순서대로 들어있기 때문에, 따로 정렬을 해줄 필요는 없다.
"""
#from collections import defaultdict
#def solution(gems):
#    answer = []
#    types = len(set(gems))
#    length = len(gems)
#    start = 0
#    end = 0
#
#    gems_dict = defaultdict(int)
#    possibles = []
#    while True:
#        current_types = len(gems_dict)
#
#        if start == length:
#            break
#
#        if current_types == types:
#            possibles.append((start+1, end))
#            gems_dict[gems[start]] -= 1
#            if gems_dict[gems[start]] == 0:
#                del gems_dict[gems[start]]
#            start += 1
#            print(start, end, possibles, gems_dict)
#            continue
#
#        if end == length:
#            break
#
#        if current_types != types:
#            gems_dict[gems[end]] += 1
#            end += 1
#            
#        print(start, end, possibles, gems_dict)
#
#
#    distance = float('inf')
#
#    print(possibles)
#    for start, end in possibles:
#        if end - start < distance:
#            answer = [start, end]
#            distance = end - start
#
#    print(answer)
#    return answer