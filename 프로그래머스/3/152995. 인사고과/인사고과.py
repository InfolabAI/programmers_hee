def solution(scores):
    return

def solution_251028(scores):
    answer = 1
    ma, mb = scores[0]
    del scores[0]
    scores = sorted(scores, key=lambda x:(-x[0], x[1]))
    maxb = 0 
    
    #print(ma, mb, scores)
    for i in range(len(scores)):
        ca, cb = scores[i]
        if ca > ma and cb > mb:
            return -1
        
        if cb >= maxb:
            maxb = cb
            if ca+cb > ma+mb:
                answer += 1
        
        #print(ca, cb, answer)
    
    return answer

# 240926
def solution_240926(scores):
    # 다른 임의의 사원보다 두 점수가 모두 낮은 경우가 한 번이라도 있다면 그 사원은 인센티브를 받지 못함
    # 인센티브 받는 사람 중 두 점수의 합이 높은 순으로 석차를 냄
    # 점수 a 로 내림차순 정렬, 점수 b 로 오름차순 정렬
    st_a, st_b = scores[0]  # 첫 번째 사원의 a, b 점수를 기준(즉, '나'의 점수)으로 저장
    scores = sorted(scores, key=lambda x: (-x[0], x[1]))  # a는 내림차순, b는 오름차순으로 정렬
    #print(scores)
    answer = 1  # 내 등수를 1등으로 초기화

    maxb = 0  # 현재까지의 b 점수 중 최대값을 저장할 변수 (인센티브 가능한 최대 b)
    for sc in scores:  # 정렬된 모든 사원을 순회
        a, b = sc  # 각 사원의 a, b 점수를 분리
        if st_a < a and st_b < b:  # 만약 나보다 두 점수 모두 높은 사원이 있다면
            return -1  # 나는 인센티브를 받을 수 없으므로 -1 반환

        # 과거 주석: 단순히 점수 합으로 비교하면 안 됨 (인센티브 미대상자는 등수에 포함되지 않기 때문)(“나보다 점수 합이 높다고 해서 꼭 등수가 높은 것은 아니다.”)
        #if sc[0] + sc[1] > st_a + st_b:
        #    answer += 1

        if b >= maxb:  # 현재 사원의 b 점수가 지금까지의 최대 b 이상이면
            maxb = b  # 최대 b 값 갱신
            if a + b > st_a + st_b:  # 이 사원의 총합 점수가 나보다 높으면
                answer += 1  # 등수 +1

    return answer  # 계산된 내 등수 반환









# 240923
#def solution(scores):
#    answer = 1
#    ta, tb = scores[0]
#    scores = sorted([[i, score] for i, score in enumerate(scores)], key=lambda x:(-x[1][0],x[1][1])) # NOTE 틀린 부분. 정렬 방법. 첫번째에 대해 내림차순. 두번째에 대해 오름차순 정렬 필요. 정렬을 이렇게 하면, 첫 번재 a는 항상 앞a >= 뒤a 가 보장되므로, 두 번재는 이전까지의maxb <= 뒤b 이면 인센티브 대상이 됨. 반대로 이전까지의maxb > 뒤b 이면 인센티브 못 받음. [[3,2], [3,1]] 같은 예외는 없음 두 번째가 오름차순이니까.
#    #print(scores)
#    mina, maxb = 10000001, -1
#    for i, [idx, [a, b]] in enumerate(scores):
#        if ta < a and tb < b: # NOTE 틀린 부분. 모든 원소와 비교해야 함.
#            return -1
#        
#        if b >= maxb:
#            maxb = b # NOTE 틀린 부분. 여기서 삽입하면 max(maxb, b) 효과가 있음.
#            if ta + tb < a + b: # NOTE 틀린 부분. 두 원소의 합이 원호보다 높을때만 answer += 1 을 해야 함.
#                answer += 1
#            
#    return answer

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


def solution(scores):
    #return solution_240926(scores)
    return solution_251028(scores)