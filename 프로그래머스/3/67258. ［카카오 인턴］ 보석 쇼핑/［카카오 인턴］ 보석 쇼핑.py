def solution(gems):
    answer = []
    return answer

# 240527 이중 loop 사용함 일부 테케 틀림. 일부 시간 초과.   
# 240528 loop 하나 사용했지만, 일부 테케 틀림. 일부 시간 초과. 테케 추가 후, append 수정하고, while 문 조건 수정해서 모든 테케 통과했지만, 효율성 통과 못함.set 으로 중복제거하는 것은 너무 느림
from collections import defaultdict
from heapq import heappush
def gems_to_dict(gems, dict_):
    for gem in gems:
        dict_[gem] += 1
        
def solution(gems):
    answers = []
    all_gems = defaultdict(int)
    gems_to_dict(gems, all_gems)
    i, j = 0, 0
    #print(all_gems)
    cur_gems = defaultdict(int)
    cur_gems[gems[0]] += 1
    if len(all_gems.keys()) == 1:
        return [1,1]
    #print(sum([v for k, v in all_gems.items()]))
    while i<=j and j < len(gems):
        #print(i, j, cur_gems)
        if len(cur_gems) != len(all_gems):
            #print("j++ ", end='')
            if i > 0:
                # heap 기준(길이), i 위치, j 위치 를 넣음
                heappush(answers, [j-(i-1), i-1,j]) # NOTE 틀린 부분. append 시점 1. j 가 찾아진 후, i 를 늘리며 좁히다가 다시 j 를 늘릴 때
            j += 1
            if j != len(gems):
                cur_gems[gems[j]] += 1
        else:
            #print("i++ ", end='')
            cur_gems[gems[i]] -= 1
            if cur_gems[gems[i]] <= 0:
                del cur_gems[gems[i]]
            i += 1
            
    #print(answers)
    if len(answers) == 0:
        return [1, len(gems)] # NOTE 틀린 부분. append 시점 2. j 가 찾아진 후, i 를 늘리는 상황이 한 번도 없을 때
    
    # NOTE 틀린 부분. 빠르게 만들기 위해 마지막에 sort 를 제외하고 heap 으로 처리했는데도 틀림.
    a1, a2 = answers[0][1]+1, answers[0][2]+1
    #print(answers)
    return [a1, a2]


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