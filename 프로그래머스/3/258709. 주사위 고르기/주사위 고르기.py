# 240503
from itertools import combinations, product
from collections import defaultdict
def get_win_num(ssums, osums):
    win_num = 0
    for os, on in osums.items():
        for ss, sn in ssums.items():
            if ss > os:
                win_num += sn*on # NOTE 틀린 부분. Compuation cost 를 줄이는 방법 두 가지. 1) 모든 경우의 수에 대해  binary search. 2) 합이 같은 경우를 하나로 묶고, 곱을 통해 전체 경우의 수 연산. 예를 들어, osums 중 2가 5개, ssums 중 3이 3개면 ssums 가 3*5=15번 이긴 것
    return win_num
        
def get_sums(sdice):
    sums = defaultdict(lambda:0)
    for vals in product(*sdice):
        sums[sum(vals)] += 1
    return sums

def select_dice(dice):
    for sids in combinations(range(len(dice)), len(dice)//2):
        oids = set(range(len(dice))) - set(sids)
        yield sids, oids
        
def solution(dice):
    best_num = 0
    for sids, oids in select_dice(dice):
        sdice = [dice[i] for i in sids]
        odice = [dice[i] for i in oids]
        win_num = get_win_num(get_sums(sdice), get_sums(odice))
        if win_num > best_num:
            answer = [sids[i] + 1 for i in range(len(sids))]
            best_num = win_num
    
    return answer
#def solution(dice):
#    return

#from itertools import combinations
#
## 특정 값보다 미만인 주사위 합의 카운트를 리턴하는 이진탐색 함수.
#def binary_search(target, case):
#    low = 0
#    high = len(case) - 1
#
#    while low <= high:
#        mid = (low + high) // 2
#
#        if case[mid] < target:
#            low = mid + 1
#        else:
#            high = mid - 1
#
#    return low
#
## 현재 조합으로 나올 수 있는 눈의 조합을 리턴하기.
#def simulate(case, dice, idx, now, out):
#    if idx == len(case):
#        out.append(now)
#        return
#
#    for d in dice[case[idx]]:
#        simulate(case, dice, idx + 1, now + d, out)
#
#def solution(dice):
#    answer = []
#
#    #주사위를 선택할 수 있는 조합을 구하기. 반대편 조합은 대칭으로 이루어져있음.
#    half = len(dice) // 2
#    selected_cases = list(combinations(list(range(len(dice))), half))
#
#    #각 조합별로 시뮬레이선 수행하여 합산 값 구하기.
#    sum_cases = {}
#    for idx, case in enumerate(selected_cases):
#        out = []
#        simulate(case, dice, 0, 0, out)
#        out.sort() #이분탐색을 위해 정렬 수행.
#        sum_cases[idx] = out
#
#    print(sum_cases)
#    # 조합을 순회하면서, 가장 많이 이기는 경우를 찾아냄.
#    bestest_sum = 0
#    for key, value in sum_cases.items():
#        #현재 케이스
#        now_case = value
#        #상대방 케이스
#        other_case = sum_cases[len(selected_cases) - key - 1]
#        print(now_case, "\n", other_case)
#
#        # 현재 케이스를 순회하면서, 상대방 케이스에서 이기는 경우를 합산할 것!
#        temp_sum = 0
#        for c in now_case:
#            temp_sum += binary_search(c, other_case)
#
#        #최고기록보다 더 많이 이겼다면, 정답 갱신
#        if temp_sum > bestest_sum:
#            bestest_sum = temp_sum
#            best_case = selected_cases[key]
#            answer = list(map(lambda x : x + 1, sorted(best_case[:])))
#
#    return answer


# 240430
###########def get_win_rate_sums(sums1, sums2): # NOTE 틀린 부분. 모든 경우의 수에 대한 sum 을 구하고 그 모든 sum 에 대해 win_rate 를 구하면 너무 느림.
###########    wins = 0
###########    for s in sums2:
###########        wins += (sums1>s).sum() # NOTE 틀린 부분. list for loop 2개보다, np 이용한 loop 1개가 빠름
###########    return wins/len(sums2)
###########
###########def get_sums(selected_dices):
###########    sums = []
###########    for nums in product(*selected_dices): # NOTE 틀린 부분. 여기가 문제다. 모든 product cases 에 대한 sum 을 찾는 것
###########        sums.append(sum(nums))
###########    #print(len(sums))
###########    #sums = list(set(sums)) # NOTE 틀린 부분. set 으로 바꿔서 중복 제거하면 시간 초과는 해결되지만, win rate 를 정확히 계산할 수 없음
###########    sums.sort()
###########    return np.array(sums)
#from itertools import product, combinations, permutations
#from collections import Counter
#import itertools, collections
#import numpy as np
#
#
#def binary_search(target, case):
#    low = 0
#    high = len(case) - 1
#
#    while low <= high:
#        mid = (low + high) // 2
#
#        if case[mid] > target:  # NOTE 틀린 부분. 큰 것부터 배치되어 있으므로, 조건문을 잘 생각해야 함.
#            low = mid + 1
#        else:
#            high = mid - 1
#
#    return low
#        
#    
#def get_win_rate(sd1, sd2):
#    wins = 0
#    # NOTE 틀린 부분. 정렬하고 나서 product 하면 자연스럽게 합이 작은 순으로 정렬됨
#    # 예., [(1, 3), (1, 3), (1, 3), (1, 3), (1, 4), (1, 4), (2, 3), (2, 3), (2, 3), (2, 3), (2, 4), (2, 4), (3, 3), (3, 3), (3, 3), (3, 3), (3, 4), (3, 4), (4, 3), (4, 3), (4, 3), (4, 3), (4, 4), (4, 4), (5, 3), (5, 3), (5, 3), (5, 3), (5, 4), (5, 4), (6, 3), (6, 3), (6, 3), (6, 3), (6, 4), (6, 4)]
#    sd1, sd2 = list(product(*sd1)), list(product(*sd2))
#    sd1 = list(map(sum, sd1))
#    sd2 = list(map(sum, sd2))
#    sd1.sort(reverse=True) # NOTE 틀린 부분. 큰 것부터 배치해야 승을 구할 수 있음. 승+무 가 아니라 정확히 승수를 구해야 함
#    sd2.sort(reverse=True)
#    prev = [0,0]
#    for ds in sd2:
#        if prev[0] == ds:
#            pass
#        else:
#            prev[1] = binary_search(ds, sd1)
#        wins += prev[1]
#    return wins
#
#def get_cases_selection(dice):
#    for ids in combinations(range(len(dice)), len(dice)//2): # NOTE 틀린 부분. permutations 가 아니라 combinations 가 중복을 제외함
#        selected_dices, other_dices = [], []
#        ids = list(ids)
#        other_ids = list(Counter(list(range(len(dice)))) - Counter(ids))
#        for i in ids:
#            selected_dices.append(dice[i])
#        for i in other_ids:
#            other_dices.append(dice[i])
#        for i in range(len(ids)): # 숫자 보정
#            ids[i] += 1
#            other_ids[i] += 1
#        #print(ids, other_ids)
#        yield selected_dices, other_dices, ids, other_ids
#
#def solution(dice):
#    best_rate = 0
#    answer = None
#    for i, (selected_dices, other_dices, ids, oids) in enumerate(get_cases_selection(dice)):
#        #print(selected_dices)
#        rate = get_win_rate(selected_dices, other_dices)
#        #rate = get_win_rate_sums(get_sums(selected_dices), get_sums(other_dices))
#        #print(rate)
#        if rate > best_rate:
#            best_rate = rate
#            answer = ids
#            
#    return answer

# 240503
#from itertools import combinations, product
#from collections import defaultdict
#def get_win_num(ssums, osums):
#    win_num = 0
#    for os, on in osums.items():
#        for ss, sn in ssums.items():
#            if ss > os:
#                win_num += sn*on # NOTE 틀린 부분. Compuation cost 를 줄이는 방법 두 가지. 1) 모든 경우의 수에 대해  binary search. 2) 합이 같은 경우를 하나로 묶고, 곱을 통해 전체 경우의 수 연산. 예를 들어, osums 중 2가 5개, ssums 중 3이 3개면 ssums 가 3*5=15번 이긴 것
#    return win_num
#        
#def get_sums(sdice):
#    sums = defaultdict(lambda:0)
#    for vals in product(*sdice):
#        sums[sum(vals)] += 1
#    return sums
#
#def select_dice(dice):
#    for sids in combinations(range(len(dice)), len(dice)//2):
#        oids = set(range(len(dice))) - set(sids)
#        yield sids, oids
#        
#def solution(dice):
#    best_num = 0
#    for sids, oids in select_dice(dice):
#        sdice = [dice[i] for i in sids]
#        odice = [dice[i] for i in oids]
#        win_num = get_win_num(get_sums(sdice), get_sums(odice))
#        if win_num > best_num:
#            answer = [sids[i] + 1 for i in range(len(sids))]
#            best_num = win_num
#    
#    return answer