def solution(sequence):
    answer = 0
    return answer

# 24072x.
# 점화식. pulse+1 일때의 min 값, pulse-1 일때의 min 값을 계속 쌓아나간다
def solution(sequence):
    answer = 0
    s1, s2, s1mn, s2mn = 0, 0, 0, 0
    pulse = 1
    for s in sequence:
        s1 += s * pulse
        s2 += s * -pulse
        
        answer = max(answer, s1-s1mn, s2-s2mn)
        
        s1mn = min(s1mn, s1)
        s2mn = min(s2mn, s2)
        #print(answer, s1, s2, s1mn, s2mn)
        
        pulse *= -1
    return answer
    

# ref (https://velog.io/@jaehyeonkim2358/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python-%EC%97%B0%EC%86%8D-%ED%8E%84%EC%8A%A4-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4%EC%9D%98-%ED%95%A9)
#from sys import maxsize
#
#INF = maxsize
#
#def solution(sequence):
#    answer = -INF
#    size = len(sequence)
#    s1 = s2 = 0				# 1
#    s1_min = s2_min = 0		# 2
#    pulse = 1
#    
#    for i in range(size):
#        s1 += sequence[i] * pulse
#        s2 += sequence[i] * (-pulse)
#        
#        # 3
#        answer = max(answer, s1-s1_min, s2-s2_min)
#        
#        # 4
#        s1_min = min(s1_min, s1)
#        s2_min = min(s2_min, s2)
#        
#        # 5
#        pulse *= -1
#    return answer

# 240723. 정답이지만, 실행시간 초과. 모든 경우의 수를 계산하지 말고, 효율적인 구현하는 것이 필요.
# NOTE 틀린부분. 모든 경우의 수를 계삲하지 말고, 점화식을 수행해야 함.
#def sum_(subseq):
#    i, j = 1, -1
#    ti, tj = 0, 0
#    for s in subseq:
#        ti += s*i
#        tj += s*j
#        i, j = i*-1, j*-1
#    return ti, tj
#
#def sliding(seq, window):
#    st, ed = 0, window
#    while ed <= len(seq):
#        yield seq[st:ed]
#        st, ed = st+1, ed+1
#def solution(sequence):
#    answer = 0
#    max_ = 0
#    for n in range(1, len(sequence)+1):
#        for s in sliding(sequence, n):
#            tm = max(sum_(s))
#            if tm > max_:
#                max_ = tm
#    
#    return max_