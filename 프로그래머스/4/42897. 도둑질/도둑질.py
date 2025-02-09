#def solution(a):
#    return 0

# 250209
def solution(a):
    """
    [문제 설명]
    - 집들이 원형으로 배치되어 있고, 인접한 집을 동시에 털면 경보가 울린다.
    - 따라서 원형 구조 특성상 '첫 번째 집을 털면 마지막 집은 털 수 없다'는 제약이 생긴다.
    - 이를 해결하기 위해 '첫 집을 터는 경우'와 '첫 집을 안 터는 경우'로 나누어 각각의 최대값을 계산한 뒤,
      두 경우 중 최댓값을 결과로 반환한다.

    [현재 코드: x1, y1, z1, x2, y2, z2 사용]
    - x1, y1, z1: "첫 번째 집을 털었다" 가정 하에 진행되는 DP 계열 변수 3개
    - x2, y2, z2: "첫 번째 집을 안 털었다" 가정 하에 진행되는 DP 계열 변수 3개

    [왜 6개의 변수가 사용되는가?]
    - 코드 작성자가 '최대값을 갱신하기 위해 i-1, i-2'를 일일이 변수로 들고 다니는 식으로 구현하였기 때문.
    - dp[i] = max(dp[i-1], dp[i-2] + a[i]) 형태를 직접 '세 자리'로 unrolling 한 듯한 형태로 보인다.
      (x, y, z 등을 회전시키며 갱신)

    [질문: x1, y1, x2, y2 만으로도 가능하지 않나?]
    - 충분히 가능하다. 일반적인 `dp[i] = max(dp[i-1], dp[i-2] + money[i])` 방식을 사용하면,
      i-1, i-2 상태만 추적하면 되므로 2개의 값만 유지해도(혹은 한정된 길이라면 배열로) 풀 수 있다.
    - 원형 구조 처리는 "첫 집을 포함해서 계산" vs "첫 집을 제외하고 계산"의 두 번의 선형 DP를 구한 뒤
      최댓값을 비교하는 방식으로 간단히 구현 가능하다.
    - 아래 예시로 (1) 첫 집 포함(linear DP, 마지막 집 제외), (2) 첫 집 미포함(linear DP, 0번 집 제외, 마지막 집 포함)을 각각 구해 비교하면 된다.

    [현재 코드 동작 흐름 요약]
    - x1, y1, z1 = a[0], a[1], (a[0] + a[2]) 형태로 초기화 (첫 집 포함)
    - x2, y2, z2 = 0, a[1], a[2] 형태로 초기화       (첫 집 미포함)
    - 이후 반복문에서 각 m에 대해:
        x1, y1, z1 = y1, z1, max(x1, y1) + m
        x2, y2, z2 = y2, z2, max(x2, y2) + m
      로 갱신
    - 최종적으로 max(x1, y1, y2, z2)를 반환

    ※ 결론적으로 x1, y1, z1, x2, y2, z2 같은 6개의 변수가 아니라
       '첫 집 포함' DP 1세트, '첫 집 미포함' DP 1세트(각각 i-1, i-2 정도만 관리)로
       충분히 구현할 수 있다.
    """

    # 초기화
    x1, y1, z1 = a[0], a[1], max(0, a[0]) + a[2]
    x2, y2, z2 = 0, a[1], a[2]

    # a[3]부터 순차적으로 DP 갱신
    for m in a[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1) + m
        x2, y2, z2 = y2, z2, max(x2, y2) + m
        # 중간 디버깅을 원하면 주석 해제
        # print(x1, y1, z1, x2, y2, z2)

    # 첫 집을 털었을 때의 케이스: 마지막 집은 못 턴다 -> 결과는 x1, y1 중 선택
    # 첫 집을 안 털었을 때의 케이스: 마지막 집까지 포함 가능 -> 결과는 y2, z2 중 선택
    # 여기서는 그대로 4개 중 최댓값을 반환
    return max(x1, y1, y2, z2)

# 250209 더 간단한 예시
def simple_linear_dp(money):
    # money 배열에 대해 dp[i] = i번째 집까지 고려했을 때의 최대값
    n = len(money)
    dp = [0]*n
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    return dp[-1]

def solution(money):
    # 1) 첫 집 포함(0~n-2)
    case1 = simple_linear_dp(money[:-1])
    # 2) 첫 집 미포함(1~n-1)
    case2 = simple_linear_dp(money[1:])
    return max(case1, case2)



## 240229
#def solution(a):
#    """
#    첫 집 텀
#    첫 집 제외
#    한 집 지나 텀
#    두 집 지나 텀
#    """
#    x1, y1, z1 = a[0], a[1], max(0, a[0]) + a[2]
#    x2, y2, z2 = 0, a[1], max(0, 0) + a[2]
#    for m in a[3:]:
#        x1, y1, z1 = y1, z1, max(x1, y1) + m
#        x2, y2, z2 = y2, z2, max(x2, y2) + m
#        #print(x1, y1, z1, x2, y2, z2)
#    
#    return max(x1, y1, y2, z2)





















# 짦은 풀이
#def solution(a):
#    x1, y1, z1 = a[0], a[1], a[0]+a[2] 			# 첫 번째 집을 선택했을 경우, 사실상 z1 = max(0, a[0]) + a[2]
#    x2, y2, z2 = 0, a[1], a[2] 					# 첫 번째 집을 선택하지 않았을 경우, 사실상 z2 = max(0, 0) + a[2]
#    for money in a[3:]:
#        x1, y1, z1 = y1, z1, max(x1, y1)+money 	# 왜 max(x1, y1) 이지? 현재 money 의 전전집은 y1 이고 x1 은 관련이 없지 않나? A: 꼭 한 집 건너 턴다는 보장은 없음. x1 털고, 두집 건너 터는 것과 y1 털고 한 집 건너 터는 것 사이의 max 값을 구하는 것
#        x2, y2, z2 = y2, z2, max(x2, y2)+money
#    return max(x1, y1, y2, z2) 					
#	# 왜 z1, x2 는 제외했지?
#    # 내 생각인데, 첫 번째 집을 선택시 마지막 집은 안 터니까 z1 제외
#    # 첫 번재 집을 선택하지 않을 시, 첫 번째 집을 의미하는 x2 는 제외

# 긴 풀이
#def solution(money):
#    length = len(money)
#    # dp배열 2개를 선언한다.
#    # dp1 배열은 0번째 집을 터는 경우이다. 따라서, 마지막 집은 털지 않는다
#    # dp2 배열은 0번째 집을 털지 않는 경우이다. 따라서, 경우에 따라 마지막 집을 털 수도 있다.
#    dp1 = [0] * length
#    dp2 = [0] * length
#
#    # dp1 배열은 첫 집을 턴다고 가정했기 때문에, dp[0]의 값을 money[0]으로 초기화한다. 
#    dp1[0] = money[0]
#
#    # 0번부터, len(dp1)-2까지 순회한다. 따라서, dp1[-1]은 0이 들어간다. 그러므로 결과값을 정할 때 dp1[-2]를 사용해야 한다
#    for i in range(0, len(dp1)-1):
#        # dp1[i]를 정함에 있어서, 그 dp[i-2] + money[i]와, dp[i-1]을 비교하는 것과 같다.
#        # 이 코드에서는 처음 원소와 마지막 원소가 연결되어 있는 것으로 간주해야하므로, 원형 큐의 형식으로 구현했다.
#        # 굳이 그럴 필요는 없는 것 같다. 
#        dp1[i] = max(dp1[(i + length - 1) % length],
#                     dp1[(i + length - 2) % length] + money[i])
#        
#    # 첫 집을 털지 않는 경우이기 때문에 , 1부터 반복하고 len(dp2)-1까지 반복한다. 
#    for i in range(1, len(dp2)):
#        # 위와 비슷하다.
#        dp2[i] = max(dp2[(i + length - 1) % length],
#                     dp2[(i + length - 2) % length] + money[i])
#
#    #print("dp1[-2]: ", dp1)
#    #print("dp2[-2]: ", dp2)
#
#    # 두 값중 큰 값을 출력한다. 
#    answer = max(dp1[-2], dp2[-1])
#
#    #money = [1,2,3,1,5]
#    #print("정답: ", solution(money))
#    return answer

# 240123 버전
#def solution(a):
#    x1, y1, z1 = a[0], a[1], max(0, a[0])+a[2]
#    x2, y2, z2 = 0, a[1], max(0, 0)+a[2]
#    i = 3
#    #print(x1, y1, z1, x2, y2, z2)
#    while i < len(a):
#        x1, y1, z1 = y1, z1, max(x1, y1)+a[i]
#        x2, y2, z2 = y2, z2, max(x2, y2)+a[i]
#        #print(x1, y1, z1, x2, y2, z2)
#        i += 1
#        
#    return max(x1, y1, y2, z2)

# 240228
#def solution(a):
#    x1, y1, z1 = a[0], a[1], max(0, a[0]) + a[2]
#    x2, y2, z2 = 0, a[1], max(0, 0) + a[2] # NOTE 틀린 부분. a[1] 과 상관없이, a[-1] > a[2] 와 a[0] > a[2] 사이의 max 를 구하는 것
#    for m in a[3:]:
#        x1, y1, z1 = y1, z1, max(x1, y1) + m 
#        x2, y2, z2 = y2, z2, max(x2, y2) + m
#        #print(f"1: {x1} {y1} {z1}\n2: {x2} {y2} {z2}")
#        
#    return max(x1, y1, y2, z2) # NOTE 틀린 부분.

