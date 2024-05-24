def solution(gems):
    answer = []
    return answer

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