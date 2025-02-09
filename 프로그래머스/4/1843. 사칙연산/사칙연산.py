#def solution(arr):
#    return 0
# 250209
def solution(arr):
    """
    [점화식 유도 개념]
    1) '-' 기호를 기준으로 식을 블록 단위로 분할합니다. 
       예: "1-3+5-8" -> ["1", "3+5", "8"]
       - 제일 왼쪽 블록(예: "1+2+3")은 모든 '+'항을 더한 값을 a0로 둡니다.

    2) 나머지 블록들은 실제로는 식에서 뺄셈 기호로 연결된 덩어리들이므로, 
       각 블록 c를 '+' 기호로 분리한 리스트 pr = [p1, p2, ...] 에 대해
         - 모든 항을 한 덩어리로 묶으면 -sum(pr)이 됩니다. (min_sub)
         - 맨 첫 항만 음수로, 나머지는 양수로 처리하면 -p1 + (p2 + p3 + ...) 이 됩니다. (max_sub)

    3) 이 (max_sub, min_sub)를, 이전까지 계산해 놓은 (max_tail, min_tail)에 결합하여
       (new_max_tail, new_min_tail)을 아래 점화식으로 갱신합니다.
         - new_max_tail = max( max_sub + max_tail,  min_sub - min_tail )
         - new_min_tail = min( min_sub - max_tail,  min_sub + min_tail )
       (동시에 갱신해야 하므로 임시변수를 사용)

    4) 모든 블록에 대해 반복 후, 최종 답은 a0 + max_tail 입니다.

    -------------------------------------------------
    [예시 1] arr = ["1", "-", "3", "+", "5", "-", "8"]
      식: 1 - 3 + 5 - 8

      1) minus_arr = ["1", "3+5", "8"]
         a0 = sum(["1"]) = 1
         max_tail = 0, min_tail = 0 (초기화)

      2) 오른쪽에서부터 블록 순회
         (1) mr = "8"
             pr = [8]
             max_sub = -8         # 첫 항만 음수
             min_sub = -8         # 전체를 묶은 음수
             new_max_tail = max(-8 + 0, -8 - 0) = -8
             new_min_tail = min(-8 - 0, -8 + 0) = -8
             => max_tail = -8, min_tail = -8

         (2) mr = "3+5"
             pr = [3, 5]
             max_sub = -3 + 5 = 2
             min_sub = -(3+5) = -8
             new_max_tail = max(2 + (-8), -8 - (-8)) = max(-6, 0) = 0
             new_min_tail = min(-8 - (-8), -8 + (-8)) = min(0, -16) = -16
             => max_tail = 0, min_tail = -16

      3) 최종 값 = a0 + max_tail = 1 + 0 = 1

    [예시 2] arr = ["5", "-", "3", "+", "1", "+", "2", "-", "4"]
      식: 5 - 3 + 1 + 2 - 4
      위 로직대로 점화식을 적용하면, 결과의 최댓값은 3이 됩니다.
    -------------------------------------------------
    """

    # 1. 주어진 배열을 문자열로 결합 -> '-' 기준으로 분리
    expression = "".join(arr)             # 예: ["1","-","3","+","5","-","8"] -> "1-3+5-8"
    minus_arr = expression.split("-")     # 예: "1-3+5-8" -> ["1", "3+5", "8"]

    # 2. 가장 왼쪽 블록(plus 덩어리)은 모두 더한 값을 a0로 둠
    a0 = sum(map(int, minus_arr[0].split("+")))

    # 3. max_tail, min_tail: '뒤 블록'들을 처리했을 때의 최대값/최솟값
    max_tail, min_tail = 0, 0

    # 4. 오른쪽 블록부터(뒤에서 앞으로) 순회하며 점화식 적용
    for mr in reversed(minus_arr[1:]):
        # 블록 mr를 '+'로 분해
        pr = list(map(int, mr.split("+")))

        # 블록 mr 전체를 음수로 묶었을 때
        min_sub = -sum(pr)
        # 첫 항만 음수, 나머지는 양수로 봤을 때 (예: 3+5 -> -3 + 5)
        max_sub = -pr[0] + sum(pr[1:])

        # 2개의 값(max_sub, min_sub)을 기존 tail과 결합
        new_max_tail = max(max_sub + max_tail,   # (현재 블록의 max_sub) + (기존 max_tail)
                           min_sub - min_tail)   # (현재 블록의 min_sub) - (기존 min_tail)
        new_min_tail = min(min_sub - max_tail,   # (현재 블록의 min_sub) - (기존 max_tail)
                           min_sub + min_tail)   # (현재 블록의 min_sub) + (기존 min_tail)

        # 동시에 갱신
        max_tail, min_tail = new_max_tail, new_min_tail

    # 5. 최종 결과 = a0 + max_tail
    return a0 + max_tail


# 240220
#def solution(arr):
#    """
#    1-(3)+5, +tail : max_sub + tail
#    1-(3+5, tail)  : min_sub - tail
#    max_tail 은 max(max_sub+max_tail, min_sub-음수min_tail)
#    min_tail 은 min(min_sub-max_tail, min_sub+음수min_tail)
#    """
#    minus_arr = "".join(arr).split("-")
#    a0 = sum(list(map(int, minus_arr[0].split('+'))))
#    max_tail, min_tail = 0,0
#    for mr in minus_arr[:0:-1]:
#        pr = list(map(int, mr.split('+')))
#        max_sub = -pr[0] + sum(pr[1:])
#        min_sub = -sum(pr)
#        max_tail, min_tail = max(max_sub+max_tail, min_sub-min_tail), min(min_sub-max_tail, min_sub+min_tail) # NOTE 틀린부분. max_tail, min_tail 계산이 서로 의존성이 있으므로, 동시에 계산해야 함
#        #print('arr', mr, '초항', a0, 'pr', pr, ' > ', min_sub, max_sub, ' > ', min_tail, max_tail)
#        
#    return a0 + max_tail










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

