def solution(gems):
    answer = []
    return answer

# 240527 일부 테케 틀림. 일부 시간 초과.   
def solution(gems):
    answers = []
    all_gems = set(gems)
    if len(all_gems) == 1:
        return [1,1]
    i, j = 0, len(gems)
    for j in list(range(j))[::-1]:
        if set(gems[:j]) != all_gems:
            j += 1
            answers.append([i, j])
            break
            
    #print(i, j, answers)
    while j != len(gems):
        while i < j:
            i += 1
            #print(i, j, answers)
            if set(gems[i:j]) != all_gems:
                ap = [i-1, j]
                answers.append(ap)
                #print("append", ap)
                break
        while j != len(gems):
            j += 1
            #print(i, j, answers)
            if set(gems[i:j]) == all_gems:
                ap = [i, j]
                answers.append(ap)
                #print("append", ap)
                break
            
    answers = sorted(answers, key=lambda x:x[1]-x[0])
    answer = answers[0]
    answer[0] += 1
    return answer


# ref (https://velog.io/@qkre/%EC%B9%B4%EC%B9%B4%EC%98%A4-Python-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%B8%ED%84%B4%EC%8B%AD-%EB%B3%B4%EC%84%9D-%EC%87%BC%ED%95%91)
"""
- 가장 처음으로 모든 보석이 모이는 종점을 찾고, 그 종점을 기준으로 출발점을 키워 간다. 출발점을 키워 가다, 보석이 전부 모이지 않는 경우가 발생하면 종점을 다시 늘린다.
- 이걸 반복하다 종점이 최대 크기에 도달하면 반복을 중단한다.
- 그렇게 모인 구간들의 집합에서 거리가 가장 짧은 것을 구한다. 구간들은 순서대로 들어있기 때문에, 따로 정렬을 해줄 필요는 없다.
"""
from collections import defaultdict
def solution(gems):
    answer = []
    types = len(set(gems))
    length = len(gems)
    start = 0
    end = 0

    gems_dict = defaultdict(int)
    possibles = []
    while True:
        current_types = len(gems_dict)

        if start == length:
            break

        if current_types == types:
            possibles.append((start+1, end))
            gems_dict[gems[start]] -= 1
            if gems_dict[gems[start]] == 0:
                del gems_dict[gems[start]]
            start += 1
            continue

        if end == length:
            break

        if current_types != types:
            gems_dict[gems[end]] += 1
            end += 1


    distance = float('inf')

    for start, end in possibles:
        if end - start < distance:
            answer = [start, end]
            distance = end - start


    print(answer)

    return answer