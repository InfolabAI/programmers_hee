def solution(sticker):
    s = sticker
    if len(sticker) == 1: return sticker[0]
    x1, x2 = s[0], s[0] # 처음에 0번째 선택시, 누적
    y1, y2 = 0, s[1] # 처음에 1번째 선택시, 누적
    for i in range(2, len(s)):
        # 첫번째 문제의 x 의 변화 [14, 14, 19, 25, 25, 34, 34, 44] 에서 19 -> 25 넘어가는 타이밍이 중요하다. 14 다음에 5를 고른 선택지(19)보다, 5 건너뛰고 11을 고른 선택지(25)가 더 낫다는 것을 max 를 통해 계산한 것이다.
        x1, x2 = x2, max(x2, x1+s[i]) # 즉, 문제 내 11의 자리(3)을 계산할 때, 그동안의 누적 19와 14+11 중 더 큰 값으로 x2 를 처리함
        y1, y2 = y2, max(y2, y1+s[i])
        #print(x1, x2, y1, y2, '>', i)
    
    return max(x1, y2)

# 240605 틀림. 단순하게 하나씩 건너가며 더한 것 중에 max 는 틀림
#def solution(sticker):
#    answer = 0
#    if len(sticker) % 2 == 0:
#        answer1 = 0
#        for i in list(range(len(sticker)))[::2]:
#            answer1 += sticker[i]
#        answer2 = 0
#        for i in list(range(len(sticker)))[1::2]:
#            answer2 += sticker[i]
#    else:
#        answer1 = 0
#        for i in list(range(len(sticker)))[:-1:2]:
#            answer1 += sticker[i]
#        answer2 = 0
#        for i in list(range(len(sticker)))[1:-1:2]:
#            answer2 += sticker[i]
#    return max(answer1, answer2)







# ref(https://tiktaek.tistory.com/66)
#def solution(sticker):
#    if len(sticker) == 1: return sticker[0]
#    answer = [[0 for i in range(len(sticker))] for j in range(2)]
#    answer[0][0:2] = [sticker[0], sticker[0]]
#    answer[1][1] = sticker[1]
#
#    for idx in range(2, len(sticker)):
#        answer[0][idx] = max(answer[0][idx-1], answer[0][idx-2]+sticker[idx])
#        answer[1][idx] = max(answer[1][idx-1], answer[1][idx-2]+sticker[idx])
#        print(answer)
#
#    return max(answer[0][-2], answer[1][-1])