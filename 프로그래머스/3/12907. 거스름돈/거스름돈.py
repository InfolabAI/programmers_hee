def solution(n, money):
    answer = 0
    return answer

# 240820
# [1, 2, 5]
# 점화식 공식
#거스름돈   0    1	2	3	4	5...
#1원 동전  1    1	1	1	1	1...
#2원 동전  1    1	1+1	1+1	1+2	1+2... 2 index 앞의 값이 더해지는 효과
#5원 동전  1    1	1+1	1+1	1+2	1+2+1... 5 ㅑindex 앞의 값이 더해지는 효과
#경우의 수  1    1	2	2	3	4...
def solution(n, money):
    answer = 0
    #dp = [0] + [1 for _ in range(n)] # NOTE 틀린 부분. 점화식을 더 정확히 바꿔야 함
    #for m in money:
    #    if m == 1:
    #        continue
    #    for i in range(2, n+1):
    #        dp[i] = dp[i] + i//m # NOTE 틀린 부분. 점화식을 더 정확히 바꿔야 함
    dp = [1] + [0 for _ in range(n)]
    for m in money:
        for i in range(m, n+1):
            dp[i] += dp[i-m]
        #print(m, dp)
    return dp[-1]

# ref https://letzgorats.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%97%B0%EC%8A%B5-%EA%B1%B0%EC%8A%A4%EB%A6%84%EB%8F%88Python
#def solution(n, money):
#    dp = [1] + [0] * (n)
#    for m in money:
#        for i in range(m,n+1):
#            dp[i] += dp[i - m]
#    return dp[n % 1000000007]