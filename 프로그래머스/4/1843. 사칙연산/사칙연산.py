#def solution(arr):
#    return 0
# 240220
def solution(arr):
    """
    1-(3)+5, +tail : max_sub + tail
    1-(3+5, tail)  : min_sub - tail
    max_tail 은 max(max_sub+max_tail, min_sub-음수min_tail)
    min_tail 은 min(min_sub-max_tail, min_sub+음수min_tail)
    """
    minus_arr = "".join(arr).split("-")
    a0 = sum(list(map(int, minus_arr[0].split('+'))))
    max_tail, min_tail = 0,0
    for mr in minus_arr[:0:-1]:
        pr = list(map(int, mr.split('+')))
        max_sub = -pr[0] + sum(pr[1:])
        min_sub = -sum(pr)
        max_tail, min_tail = max(max_sub+max_tail, min_sub-min_tail), min(min_sub-max_tail, min_sub+min_tail) # NOTE 틀린부분. max_tail, min_tail 계산이 서로 의존성이 있으므로, 동시에 계산해야 함
        #print('arr', mr, '초항', a0, 'pr', pr, ' > ', min_sub, max_sub, ' > ', min_tail, max_tail)
        
    return a0 + max_tail










# 이 생각을 순서대로 할 수 있어야 함
# https://school.programmers.co.kr/questions/64429
#    """
#    예) 1-3+5-8
#    + 는 결합법칙 가능, - 는 결합법칙 불가능. 즉, - 에서 괄호가 어떻게 되는지가 중요.
#    이전 - 를 tail (즉, -8), 현재 - 를 sub (즉, -3+5) 라 명명할 때, 1 의 입장.
#    	-(3+5, tail) : min_sub - tail
#        -(3+5), tail : min_sub + tail
#        -(3)+5, tail : max_sub + tail
#    max 경우, max_sub + max_tail(양수) 또는 min_sub - min_tail(음수) 중 큰 수 NOTE 틀린 부분
#    min 경우, min_sub + min_tail(음수) 또는 min_sub - max_tail(양수) 중 큰 수 NOTE 틀린 부분
#    """

# https://school.programmers.co.kr/questions/64429
#def solution(arr):
#    arr = ''.join(arr).split('-')
#    a0 = sum([*map(int, arr[0].split('+'))]) ### 초항 합계
#    min_tail, max_tail = 0, 0    
#    for a in arr[:0:-1]: ### 초항 제외 역순
#        sub = [*map(int, a.split('+'))]
#        min_sub = -sum(sub) 
#        max_sub = -2*sub[0] -min_sub
#        max_tail, min_tail = max(max_sub +max_tail, min_sub -min_tail), min(min_sub +min_tail, min_sub -max_tail)
#        print('arr', arr, '초항', a0, 'a', a, ' > ', sub, min_sub, max_sub, ' > ', min_tail, max_tail)
#    return a0 +max_tail

# 240215 25m
#def solution(arr):
#    arr = "".join(arr).split('-')
#    a0 = sum(map(int, arr[0].split('+')))
#    
#    min_tail, max_tail = 0, 0
#    for a in arr[:0:-1]: # NOTE 틀린 부분 첫 항빼고 reverse
#        a = list(map(int, a.split('+')))
#        max_sub = -a[0] + sum(a[1:])
#        min_sub = -sum(a)
#        max_tail, min_tail = max(max_sub + max_tail, min_sub - min_tail), min(min_sub + min_tail, min_sub - max_tail)
#        print('arr', arr, '초항', a0, 'a', a, ' > ', min_sub, max_sub, ' > ', min_tail, max_tail)
#    
#    return a0 + max_tail

# 240219
#def solution(arr):
#    """
#    예) 1-3+5-8
#    + 는 결합법칙 가능, - 는 결합법칙 불가능. 즉, - 에서 괄호가 어떻게 되는지가 중요.
#    이전 - 를 tail (즉, -8), 현재 - 를 sub (즉, -3+5) 라 명명할 때, 1 의 입장.
#    	-(3+5, tail) : min_sub - tail
#        -(3+5), tail : min_sub + tail
#        -(3)+5, tail : max_sub + tail
#    max 경우, max_sub + max_tail(양수) 또는 min_sub - min_tail(음수) 중 큰 수 NOTE 틀린 부분
#    min 경우, min_sub + min_tail(음수) 또는 min_sub - max_tail(양수) 중 큰 수 NOTE 틀린 부분
#    """
#
#    minus_arr = "".join(arr).split("-")
#    a0 = sum(list(map(int, minus_arr[0].split("+")))) # NOTE 틀린 부분
#    max_tail, min_tail = 0, 0
#    for mr in minus_arr[:0:-1]:
#        pr = list(map(int, mr.split("+")))
#        max_sub = -pr[0] + sum(pr[1:])
#        min_sub = -sum(pr)
#        max_tail, min_tail = max(max_sub + max_tail, min_sub - min_tail), min(min_sub+min_tail, min_sub-max_tail)
#        #print('arr', arr, '초항', a0, ' > ', min_sub, max_sub, ' > ', min_tail, max_tail)
#    
#    return a0 + max_tail

