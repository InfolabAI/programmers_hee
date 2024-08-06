def solution(sequence):
    answer = 0
    return answer

# 24072x.
# NOTE 틀린 부분. DP 임. [1, -1, 1, ...] 일때의 min 값, [-1, 1, -1, ...] 일때의 min 값을 계속 쌓아나간다
# NOTE 틀린 부분. 카데인 알고리즘의 응용임, 카데인 알고리즘은 직전 최대 부분합을 이용해서 다름 최대 부분합을 계산하는 방법임
# NOTE 틀린 부분. 펄스를 사용할 때는 최대 부분합을 찾기 위해 약간의 응용이 필요함. 그 응용이 바로 s2-s1mn, s2-s2mn 임. 펄스 이므로, 바로 이전 최소값(음수)를 뺄때가 최대값이라고 볼 수 있기 때문
"""
[2, 3, -6, ...] 일때 시뮬레이션 (answer, s1, s2, s1mn, s2mn, s1-s1mn, s2-s2mn 순)
2	2	-2	0	-2	2	0
3	-1	1	-1	-2	0	3 # 여기서 s2==1 은 누적합, s2mn==-2 는 직접최소값, s2-s2mn==3 은 최대증가폭임. 최대증가폭은 최대부분합과 동일함.
9	-7	7	-7	-2	0	9
10	-8	8	-8	-2	0	10
10	-5	5	-8	-2	3	7
10	-4	4	-8	-2	4	6
10	-2	2	-8	-2	6	4
10	-6	6	-8	-2	2	8

"""
# 240806
def solution(sequence):
    answer = 0
    pulse = 1
    s1, s2, s1mn, s2mn = 0, 0, 0, 0
    for s in sequence:
        s1 += s * pulse
        s2 += s * -pulse
        
        answer = max(answer, s1-s1mn, s2-s2mn)
        
        s1mn, s2mn = min(s1, s1mn), min(s2, s2mn)
        pulse *= -1
        #print(answer, s1, s2, s1mn, s2mn, s1-s1mn, s2-s2mn)
        
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

# 240724
#def solution(sequence):
#    answer = 0
#    s1, s2, s1mn, s2mn = 0, 0, 0, 0
#    pulse = 1
#    for s in sequence:
#        s1 += s * pulse
#        s2 += s * -pulse
#        
#        answer = max(answer, s1-s1mn, s2-s2mn) # NOTE 틀린 부분. 왜 s1-s1mn 인가?
#        
#        s1mn = min(s1mn, s1)
#        s2mn = min(s2mn, s2)
#        
#        pulse *= -1
#        #print(answer, s1, s2, s1mn, s2mn, s1-s1mn, s2-s2mn)
#    return answer