def solution(scores):
    return

# 240923
def solution(scores):
    answer = 1
    ta, tb = scores[0]
    scores = sorted([[i, score] for i, score in enumerate(scores)], key=lambda x:(-x[1][0],x[1][1])) # NOTE 틀린 부분. 정렬 방법. 첫번째에 대해 내림차순. 두번째에 대해 오름차순 정렬 필요. 정렬을 이렇게 하면, 첫 번재 a는 항상 앞a >= 뒤a 가 보장되므로, 두 번재는 이전까지의maxb <= 뒤b 이면 인센티브 대상이 됨. 반대로 이전까지의maxb > 뒤b 이면 인센티브 못 받음. [[3,2], [3,1]] 같은 예외는 없음 두 번째가 오름차순이니까.
    #print(scores)
    mina, maxb = 10000001, -1
    for i, [idx, [a, b]] in enumerate(scores):
        if ta < a and tb < b: # NOTE 틀린 부분. 모든 원소와 비교해야 함.
            return -1
        
        if b >= maxb:
            maxb = b # NOTE 틀린 부분. 여기서 삽입하면 max(maxb, b) 효과가 있음.
            if ta + tb < a + b: # NOTE 틀린 부분. 두 원소의 합이 원호보다 높을때만 answer += 1 을 해야 함.
                answer += 1
            
    return answer

#def solution(scores):
#    answer = 0
#    target_a, target_b = scores[0]
#    target_score = target_a + target_b
#
#    # 첫번째 점수에 대해서 내림차순,
#    # 첫 번째 점수가 같으면 두 번째 점수에 대해서 오름차순으로 정렬합니다.
#    scores.sort(key=lambda x: (-x[0], x[1]))
#    maxb = 0
#    
#    for a, b in scores:
#        if target_a < a and target_b < b:
#            return -1
#        
#        if b >= maxb:
#            maxb = b
#            if a + b > target_score:
#                answer += 1
#            
#    return answer + 1