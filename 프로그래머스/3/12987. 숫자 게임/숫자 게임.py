def solution(A, B):
    return answer
# 240510
def solution(A, B):
    # 예제와 다르게 해결해도 됨. 둘 다 sort 하고 큰 수부터 차례로 비교해도 정답임.
    A.sort(reverse=True)
    B.sort(reverse=True)
    i, answer = 0,0
    for a in A:
        if B[i] > a:
            i += 1
            answer += 1
    
    return answer






















# 240507
#def solution(A, B):
#    answer = -1
#    A.sort(reverse=True)
#    B.sort(reverse=True)
#    # NOTE 틀린 부분. 어떤 순서로 구해야 최소의 시간에 문제를 해결하는가? 나이브하게는 product 를 이용해야 하는뎨?
#    # A: 굳이 예제처럼 이기지 않아도 됨. A 큰 수에 대해서 B 를 큰 수부터 차례대로 출전 시키면 그게 최대 승수임.
#    answer = 0 
#    i = 0
#    for a in A:
#        if a < B[i]:
#            answer+=1
#            i+=1
#    
#    return answer


#def solution(A, B):
#    answer = 0
#    A.sort(reverse=True)
#    B.sort(reverse=True)
#    i = 0
#    for a in A:
#        if a < B[i]:
#            print(a, B[i], 'B win')
#            answer += 1
#            i += 1
#    return answer
#