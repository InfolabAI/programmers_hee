#def solution(a):
#    return 0
# 240229
def solution(a):
    """
    첫 집 텀
    첫 집 제외
    한 집 지나 텀
    두 집 지나 텀
    """
    x1, y1, z1 = a[0], a[1], max(0, a[0]) + a[2]
    x2, y2, z2 = 0, a[1], max(0, 0) + a[2]
    for m in a[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1) + m
        x2, y2, z2 = y2, z2, max(x2, y2) + m
        #print(x1, y1, z1, x2, y2, z2)
    
    return max(x1, y1, y2, z2)





















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

