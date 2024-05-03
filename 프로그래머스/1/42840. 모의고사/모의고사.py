#def solution(answers):
#    return
# 240328
import numpy as np
def solution(answers):
    n_dict = {1: [1, 2, 3, 4, 5],
              2: [2, 1, 2, 3, 2, 4, 2, 5],
              3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
             }
    
    score = [0,0,0] # NOTE 틀린 부분. 각 수포자마다 하나의 숫자를 가지를 list 를 사용하면, enumerate 를 통해, 위치를 return 할 수 있음.
    answers = np.array(answers)
    for k, v in n_dict.items():
        correct = 0
        v = np.array(v)
        while len(v) < len(answers): # NOTE 틀린 부분. numpy 를 사용한 비교식 1번 보다, list 상태로 for문 1번 돌며 숫자마다 비교하는 것이 훨씬 빠름.
            v = np.concatenate([v, v])
        score[k-1] += sum(v[:min(len(v), len(answers))] == answers[:min(len(v), len(answers))])
    
    ret = []
    for i, s in enumerate(score):
        if s == max(score):
            ret.append(i+1)
    
    return ret






















#def solution(answers):
#    #각 수포자의 패턴
#    pattern1 = [1,2,3,4,5]
#    pattern2 = [2,1,2,3,2,4,2,5]
#    pattern3 = [3,3,1,1,2,2,4,4,5,5]
#    score = [0, 0, 0]
#    result = []
#
#    #나머지 계산을 통해 위치에 맞는 정답을 pattern 과 비교함
#    for idx, answer in enumerate(answers):
#        if answer == pattern1[idx%len(pattern1)]:
#            score[0] += 1
#        if answer == pattern2[idx%len(pattern2)]:
#            score[1] += 1
#        if answer == pattern3[idx%len(pattern3)]:
#            score[2] += 1
#
#    #가장 많이 맞춘 수포자만 list에 추가시킴
#    for idx, s in enumerate(score):
#        if s == max(score):
#            result.append(idx+1)
#
#    return result



#def solution(answers):
#    human1 = [1, 2, 3, 4, 5]
#    len_human1 = len(human1)
#    human2 = [2, 1, 2, 3, 2, 4, 2, 5]
#    len_human2 = len(human2)
#    human3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#    len_human3 = len(human3)
#    correct = [0, 0, 0]
#    
#    for i, ans in enumerate(answers):
#        if human1[i%len_human1] == ans:
#            correct[0] += 1
#        if human2[i%len_human2] == ans:
#            correct[1] += 1
#        if human3[i%len_human3] == ans:
#            correct[2] += 1
#    
#    ret = []
#    for i, c in enumerate(correct):
#        if c == max(correct):
#            ret.append(i+1)
#    return ret
    
