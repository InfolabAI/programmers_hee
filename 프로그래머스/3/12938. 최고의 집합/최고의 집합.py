def solution(n, s):
    return

#240909
def solution(n, s):
    answer = []
    if (s == 1) or s < n: # NOTE 틀린 부분. 생각하지 못한 예외 상황들을 다루는 것이 필요함.
        return [-1]
    residual = 0
    for i in range(n):
        if residual == s%n: # NOTE 틀린 부분. s%n 을 최대한 1씩 각 elements 에 분배해야 곱이 최대값이 됨.
            answer += [s//n] 
        else:
            answer += [s//n + 1]
            residual += 1
    return sorted(answer)









# 240510
#import heapq as hq
#def solution(n, s):
#    # 최대한 모든 숫자가 (s//n) 에 가깝거나 1커야 곱이 가장 높음
#    nums = [s//n for _ in range(n)]
#    if sum(nums) == 0:
#        return [-1]
#    
#    for _ in range(s%n):
#        hq.heappush(nums, hq.heappop(nums)+1)
#    
#    nums.sort() # NOTE 틀린 부분. heap 은 오름차순 정렬을 보장하지 않으므로,sort 필요
#    return nums




# 240507
#def solution(n, s):
#    # 곱이 최대가 되려면 모든 수가 최대한 같은 값이어야 함. 즉, 모든 수가 int(s/n) 에 가까워야 함
#    answer = []
#    a = int(s/n)
#    if a == 0:
#        return [-1]
#    b = s%n
#    for i in range(n-b):
#        answer.append(a)
#    for i in range(b):
#        answer.append(a+1)
#    return answer

## ref1
#def solution(n, s):
#    # 자연수 n개의 합으로 n보다 작은 s를 만들 수는 없으므로 [-1]을 리턴한다
#    if n > s: return [-1]
#    result = []
#    # s를 n으로 나눈 몫이 n개이도록 초기값을 정한다.
#    initial = s // n
#    for _ in range(n):
#        result.append(initial)
#    idx = len(result) - 1
#    # s를 n으로 나눈 몫에서 나머지만큼 각 값에 1씩 더해준다.
#    for _ in range(s % n):
#        result[idx] += 1
#        idx -=1
#    return result
#
## ref2
#def bestSet(n, s):
#    answer = []
#    a = int(s/n)
#
#    if a == 0:
#        return [-1]
#
#    b = s%n
#
#    for i in range(n-b):
#        answer.append(a)
#    for i in range(b):
#        answer.append(a+1)
#
#    return answer
