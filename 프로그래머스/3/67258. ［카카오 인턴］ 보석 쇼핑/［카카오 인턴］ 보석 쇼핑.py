def solution(gems):
    answer = []
    return answer





## 241219-3  # st, ed 를 움직여가며 수행해서 훨씬 빨라졌고 답도 맞으나, 효율성은 시간 초과. dict 를 써서 중복 체크를 더 빠르게 했지만, 효율성 테스트 중 일부를 통과 못함
#from collections import defaultdict
#def get_set_len(gems_dict):
#    len_ = 0
#    for k in gems_dict:
#        if gems_dict[k] > 0:
#            len_ += 1
#    return len_
#        
## 241219 candidate sorting 을 없애도록 효율화 했으나, 그래도 효율성 테스트 통과 못함
#def solution(gems):
#    answer = []
#    st, ed = 0, 0
#    max_len = len(set(gems))
#    gems_dict = defaultdict(lambda:0)
#    gems_dict[gems[0]] += 1
#    min_cand_len = 100000
#    
#    do_ = True
#    i = 0
#    while do_:
#        if len(gems_dict) == max_len and st <= ed:
#            st += 1
#            gems_dict[gems[st-1]] -= 1
#            if gems_dict[gems[st-1]] <= 0:
#                del gems_dict[gems[st-1]]
#            if ed - st < min_cand_len:
#                candidate = (st, ed)
#                min_cand_len = ed - st
#        else:
#            ed += 1
#            if ed >= len(gems):
#                break
#            gems_dict[gems[ed]] += 1
#            
#        
#    #print(candidate)
#    #candidate = sorted(candidate, key=lambda x:x[1]-x[0])
#    return [candidate[0], candidate[1]+1]

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
"""
제공된 코드는 '투 포인터(Two Pointers)' 또는 '슬라이딩 윈도우(Sliding Window)' 알고리즘을 사용하여 문제를 해결합니다.

`start`와 `end`라는 두 개의 포인터를 사용하여 보석 배열 `gems`의 특정 구간(윈도우)을 탐색합니다.

1.  윈도우(`[start, end)`) 안에 모든 종류의 보석이 포함될 때까지 `end`를 증가시킵니다. (윈도우 확장)
2.  모든 종류가 포함되면, 해당 구간 `[start+1, end]`를 정답 후보(`possibles`)에 추가합니다.
3.  그 후, `start`를 증가시키면서 윈도우의 맨 왼쪽 보석을 제거합니다. (윈도우 축소)
4.  윈도우 축소 후에도 여전히 모든 종류의 보석이 포함되어 있다면, 이는 더 짧은 유효한 구간이므로 다시 정답 후보에 추가하고 3번을 반복합니다.
5.  윈도우 축소 후 모든 종류가 포함되지 않게 되면, 다시 1번(윈도우 확장)으로 돌아갑니다.
6.  이 과정을 `start`나 `end`가 배열 끝에 도달할 때까지 반복합니다.
7.  마지막으로, 정답 후보(`possibles`) 리스트에 저장된 모든 구간 중 가장 짧은 구간을 찾습니다. 만약 길이가 같다면, `possibles` 리스트에는 `start`가 작은 순서대로 저장되어 있으므로, 가장 먼저 찾은 구간이 정답이 됩니다.
"""

# 딕셔너리의 키가 존재하지 않을 때 기본값(int의 경우 0)을 자동으로 생성해주는 defaultdict를 임포트합니다.
from collections import defaultdict 

# 'gems' 리스트를 입력받아 [시작, 끝] 구간을 반환하는 solution 함수를 정의합니다.
def solution(gems):
    # 최종 정답 [시작 진열대 번호, 끝 진열대 번호]를 저장할 리스트입니다.
    answer = []
    
    # 'gems' 리스트에 있는 모든 보석의 '종류'가 총 몇 개인지 계산합니다. (set을 사용해 중복 제거)
    types = len(set(gems))
    
    # 'gems' 리스트(전체 진열대)의 총 길이를 저장합니다. (경계 검사용)
    length = len(gems)
    
    # 슬라이딩 윈도우(구간)의 시작 지점을 나타내는 인덱스 (0-based, inclusive)
    start = 0
    
    # 슬라이딩 윈도우(구간)의 끝 지점을 나타내는 인덱스 (0-based, exclusive)
    # 즉, 실제 윈도우의 범위는 [start, end) 입니다. (start <= index < end)
    end = 0

    # 현재 윈도우 [start, end)에 포함된 보석의 종류와 그 개수를 저장할 딕셔너리입니다.
    gems_dict = defaultdict(int)
    
    # 모든 종류의 보석을 포함하는 '가능한' 구간 [시작, 끝] (1-based)들을 저장할 리스트입니다.
    possibles = []

    # 윈도우를 이동시키기 위한 메인 루프입니다.
    while True:
        # 현재 윈도우 [start, end)에 포함된 보석의 '고유한 종류' 수입니다.
        current_types = len(gems_dict)

        # (종료 조건 1) 시작 포인터(start)가 배열의 끝에 도달하면, 더 이상 윈도우를 줄이거나 이동할 수 없으므로 루프를 종료합니다.
        if start == length:
            break

        # [윈도우 축소 단계]
        # 현재 윈도우가 모든 종류의 보석(types)을 포함하고 있는 경우
        if current_types == types:
            # 현재 윈도우 [start, end)를 1-based 인덱스로 변환하여 (start+1, end) 정답 후보 리스트에 추가합니다.
            possibles.append((start+1, end))
            
            # 윈도우를 오른쪽으로 한 칸 축소하기 위해, 가장 왼쪽(start)의 보석을 딕셔너리에서 1개 뺍니다.
            gems_dict[gems[start]] -= 1
            
            # 만약 해당 보석의 개수가 0이 되었다면 (즉, 윈도우에서 완전히 빠졌다면)
            if gems_dict[gems[start]] == 0:
                # 딕셔너리에서 이 보석 종류 자체를 삭제합니다. (current_types 계산을 정확하게 하기 위해)
                del gems_dict[gems[start]]
                
            # 시작 포인터(start)를 오른쪽으로 한 칸 이동시킵니다. (윈도우 축소)
            start += 1
            
            # (디버깅용) 현재 start, end, 후보 리스트, 보석 딕셔너리 출력 (원래 코드의 주석 처리된 부분)
            # print(start, end, possibles, gems_dict) 
            
            # 윈도우를 축소했으니, 다시 루프의 처음으로 돌아가 (축소된 윈도우가 여전히 모든 종류를 포함하는지) 확인합니다.
            continue

        # [윈도우 확장 단계의 종료 조건]
        # (종료 조건 2) 윈도우가 모든 종류를 포함하지 못했는데, 끝 포인터(end)가 배열의 끝에 도달한 경우
        if end == length:
            # 더 이상 윈도우를 확장할 수(보석을 추가할 수) 없으므로 루프를 종료합니다.
            break

        # [윈도우 확장 단계]
        # 현재 윈도우가 모든 종류의 보석을 포함하지 *못한* 경우 (그리고 end가 아직 끝이 아닌 경우)
        if current_types != types:
            # 끝 포인터(end)가 가리키는 보석을 딕셔너리에 추가 (개수 1 증가)합니다.
            gems_dict[gems[end]] += 1
            
            # 끝 포인터(end)를 오른쪽으로 한 칸 이동시킵니다. (윈도우 확장)
            end += 1
            
        # (디버깅용) 현재 start, end, 후보 리스트, 보석 딕셔너리 출력 (원래 코드의 주석 처리된 부분)
        # print(start, end, possibles, gems_dict)


    # [최종 결과 필터링]
    
    # 가장 짧은 구간의 길이(distance)를 저장할 변수. 초기값은 무한대(float('inf'))로 설정합니다.
    distance = float('inf')

    # (디버깅용) 모든 정답 후보 구간들 출력 (원래 코드의 주석 처리된 부분)
    # print(possibles)
    
    # 모든 정답 후보 구간(possibles)들을 순회합니다. (possibles는 start가 작은 순서대로 저장되어 있습니다.)
    for start, end in possibles:
        # 현재 구간의 길이(end - start)가 이전에 찾은 최소 길이(distance)보다 *짧다면*
        if end - start < distance:
            # 정답(answer)을 이 구간 [start, end]로 교체합니다.
            answer = [start, end]
            
            # 최소 길이(distance)를 현재 구간의 길이로 업데이트합니다.
            distance = end - start
        # (만약 길이가 같다면 (end - start == distance), 이 if문은 실행되지 않습니다.
        # 'possibles' 리스트는 start가 증가하는 순서대로 쌓였기 때문에,
        # 이미 answer에 저장된 구간이 start가 더 작은 구간이므로, 문제 조건(시작 진열대 번호가 가장 작은 구간)을 자동으로 만족합니다.)

    # (디버깅용) 최종 정답 출력 (원래 코드의 주석 처리된 부분)
    # print(answer)
    
    # 찾은 가장 짧은 구간 [시작, 끝]을 반환합니다.
    return answer