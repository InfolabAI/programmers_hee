#def solution(N, number):
#    return
# 240402
def calc(nums1, nums2):
    ret = []
    for x in nums1:
        for y in nums2:
            ret += [x+y]
            ret += [x-y]
            ret += [x*y]
            if y != 0:
                ret += [x//y]
                
    return set(ret)


from collections import defaultdict
def solution(N, number):
    nums = defaultdict(set)
    nums[1] = {N}
    
    if number == N:
        return 1
    
    for n in range(2, 9):
        for i in range(1, n):
            nums[n] |= calc(nums[i], nums[n-i])
        nums[n] |= {int(str(N)*n)}
        if number in nums[n]:
            return n
            
    return -1






















# 문제 풀이 방법
# 주어진 N을 1번 사용할 때부터 최대 8번 사용할 때까지 반복해서 사칙연산을 한다.
# 1번 사용할 때는 그냥 N
# 2번 사용할 때, ex: N=5, 5*5, 5+5, 5-5, 5/5 가 되므로
# 2번 사용할 때 '1번' (op) '1번' : op -> +, -, *, /, 붙이기
# 3번일 때는 '1번' (op) '2번', '2번' (op) '1번' ** 반대도 해주어야 빼기와 나누기가 계산됨
# 4번일 때는 '1번' (op) '3번', '2번' (op) '2번', '3번' (op) '1번'
# N일 때는 1 (op) N-1, 2 (op) N-2, 3 (op) N-3,... N-1 (op) 1 까지 계산해 준다.
# 매번 계산 할 때마다 결과를 set()에 넣어 주어 중복값을 없앤다.

# 1번에 계산된 값을 2번에서 사용하고 2번에 계산된 값을 3에서 사용하는 방법으로 계산
# 큰 값을 잘게 나누어 계산 하고 그 결과를 재사용할 수 있으며, 계산되는 값들이 겹치므로 DP에 해당.

#-----------------------------------------------------------------
# 저장된 값들에 대한 사칙연산 함수
# 3번 단계에서 X는 1번으로 계산된 결과, Y는 2번에 계산된 결과가 될 수 있음
# def calculate_n(X, Y):
#     n_set = set()
#     for x in X:
#         for y in Y:
#             n_set.add(x+y)
#             n_set.add(x-y)
#             n_set.add(x*y)
#             if y != 0:
#                 n_set.add(x//y)
#     return n_set
# 
# def solution(N, number):
#     answer = -1
#     result = {}   # key는 숫자 사용횟수, value는 숫자를 key번 사용했을 때 나오는 연산 결과셋
#     result[1] = {N} # N을 1번 사용할 때는 그냥 N
#     if number == N:
#         return 1
#     for n in range(2, 9):  # 8번까지만 계산하므로
#         i = 1
#         temp_set = {int(str(N)*n)}  # N=5, 2번 사용할 때 먼저 55를 저장
#         # 1 (op) N-1.... n-1 (op) 1 까지 계산
#         while i < n:
#             temp_set.update(calculate_n(result[i], result[n-i]))
#             i += 1
#         print(temp_set)
#         # 만들어진 셋에 원하는 숫자가 있으면 stop
#         if number in temp_set:
#             answer = n
#             break
# 
#         result[n] = temp_set
# 
#     return answer

#def build_set(X:list, Y:list):
#    tmp = []
#    for x in list(X):
#        for y in list(Y):
#            tmp += [x+y]
#            tmp += [x-y]
#            tmp += [x*y]
#            if y != 0:
#                tmp += [x//y]
#    return set(tmp)
#
#def solution(N, number):
#    answer = -1
#    ret = {1: {N}}
#    if number == N:
#        return 1
#    for n in range(2,9):
#        tmp = {int(str(N)*n)}
#        i = 1
#        while i < n:
#            tmp |= build_set(ret[i], ret[n-i])
#            i += 1
#            
#        ret[n] = tmp
#        #print(tmp)
#        if number in tmp:
#            answer = n
#            break
#    
#    return answer

# 240401
#from collections import defaultdict
#def calc(nums1, nums2):
#    ret = []
#    for x in nums1:
#        for y in nums2:
#            ret += [x+y]
#            ret += [x-y]
#            ret += [x*y]
#            if y != 0:
#                ret += [x//y]
#                
#    return set(ret)
#    
#def solution(N, number):
#    # number 가 5일때,
#    # 1번 사용: el 5
#    # 2번 사용: 1번 (op) 1번: op = {+, -, *, /, 붙이기}
#    # 3번 사용: 1번 (op) 2번, 2번 (op) 1번 
#    # 4번 사용: 1번 (op) 3번, 2번 (op) 2번, 3번 (op) 1번
#    # 5번 사용: 1번 (op) 4번, 2번 (op) 3번, 3번 (op) 2번, 4번 (op) 1번
#    # N번 사용: 1번 (op) N-1번, 2번 (op) N-2번, ..., N-2번 (op) 2번, N-1번 (op) 1번
#    # NOTE 5_5 를 eval 연산하면 55가 되지만, 이 문제에서는 필요없음.
#    # NOTE 틀린 부분. _, 즉, 붙이기는 기본 수 N 만 가능. 연산결과끼리(예., -5 와 -5)는 붙이지 않음.
#    nums = defaultdict(set)
#    nums[1] = set([N])
#    answer = -1
#    if number == N: # NOTE 틀린 부분. number 가 N 자체이면 바로 1을 리턴해야 함. 즉 답은, -1, 1, 2~ 가 가능하고, 2~ 는 아래 연산으로 얻어내는 것.
#        return 1
#    for n in range(2,9): # 8초과면 -1이니까
#        for i in range(1, n):
#            nums[n] |= calc(nums[i], nums[n-i]) # NOTE 틀린 부분. 1~n-1 까지에 대해 i 와 n-i 를 연산해야 함.
#        nums[n] |= set([int(str(N)*n)]) # NOTE 틀린 부분. 숫자 2개 붙이기를 언제 어디에서 추가해야 하는지를 틀렸었음.
#        #print(n, nums[n])
#        if number in nums[n]:
#            answer = n
#            break
#    return answer
            

