# 해설 https://happy-obok.tistory.com/10
#def solution(n, times):
#    return
# 240409
def solution(n, times):
    mn, mx = 0, min(n*max(times), 1e+18)  # NOTE. max 값이 1,000,000,000 * 1,000,000,000 면 너무 커짐 제한하면 더 빠름.
    while mx > mn:
        md = (mn + mx) // 2
        # md 동안 검사받을 수 있는 사람의 수를 어떻게 계산할 것인가? 애초에 이것이 정확히 계산되면 이분탐색 할 필요가 없잖은가?
        # NOTE 틀린 부분. 그냥 각 검사대가 md 동안 한번도 안 쉬었을때를 기준으로 하기. 그게 최적이니까.
        max_num = sum([md // t for t in times])
        if max_num >= n:
            mx = md
        else:
            mn = md + 1
        #print(max_num, md)
        
    return mn # NOTE 틀린 부분. return md 는 틀림. return mn 을 해야함.












#def solution(n, times):
#    min_, mid_, max_ = 0, 0, max(times)*n
#    while min_ < max_:
#        mid_ = min_ + (max_-min_)//2
#        cnt = 0
#        for t in times:
#            cnt += mid_ // t
#        print(f"{mid_}: {cnt}")
#            
#        if cnt >= n:
#            max_ = mid_
#        else:
#            min_ = mid_ + 1
#        
#    return min_








'''
https://hyem-study.tistory.com/113
가장 긴 시간이 걸리는 검사대에 모든 사람이 검사받을 경우 가장 최악의 경우일 것이다. max는 최대time*n이다. 
그리고 최소의 시간은 당장 가늠할 수 없으므로 min을 0으로 지정해둔다.
중간mid 시간을 기준으로 해당 시간까지 검사 받을 수 있는 사람의 수를 계산한다. 그 값을 cnt라고 한다.

cnt가 n보다 작다면 시간이 더 필요한 것이다. min 값을 증가 시켜준다.
cnt가 n보다 크거나 같다면 n명의 사람이 검사를 받기에 충분하다는 뜻이다.

시간을 줄여도 될 수 있기 때문에 max값을 감소시켜준다.
'''
#def solution(n, times):
#    answer = 0
#    # 여기서 min_, mid, max 는 모든 n 이 처리되는 시간을 appox 함
#    min_, mid, max_ = 0, 0, max(times)*n
#    # 무한 loop 에 빠짐. 왜?
#    # A: mid 계산을 min_, max_ 의 중간으로 해야 하는데, max_ 의 절반으로 계산했기 때문
#    i = 0
#    while min_ < max_:
#        mid = min_ + (max_-min_) // 2
#        cnt = 0
#        
#        # min 과 max 의 중간인 mid 시간동안 각 검색대에서 검사받을 수 있는 사람의 수를 더함
#        # mid 시간 동안 모든 심사위원이 한 번도 쉬지 않고 심사를 수행했을 때 총 사람 수를 구하는 것
#        for t in times:
#            cnt += mid // t
#            
#        # 만약 cnt>=n 이면 mid 가 너무 높은 것이므로, max_ 를 mid 로 낮춤
#        # 만약 cnt<n 이면 mid 가 너무 낮은 것이므로, min_ 을 mid 로 높임
#        # 여기서 >= 가 아니라 > 이면, 대부분 실패함
#        if cnt >= n:
#            max_ = mid
#        else:
#            min_ = mid + 1
#        
#    answer = min_
#    return answer


#def solution(n, times):
#    mn, md, mx = 0, 0, max(times) * n
#    while mn < mx:
#        md = mn + (mx - mn)//2
#        cnt = 0
#        
#        for t in times:
#            cnt += md // t
#            
#        #print(cnt, ":", mn, md, mx)
#        if cnt < n:
#            mn = md + 1
#        else:
#            mx = md
#        
#    return mn


