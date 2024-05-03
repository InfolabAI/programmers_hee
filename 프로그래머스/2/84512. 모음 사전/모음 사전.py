#def solution(word):
#    return 0
# 240305
def solution(word):
    """
    AAAAA to AAAAE 1
    AAAA to AAAE 1 + 1*5 > AAAA, AAAAA, AAAAE, AAAAI, AAAAO, AAAAU, AAAE
    AAA to AAE 1 + 1*5 + 1*5^2
    AA to AE 1 + (1+(1+5)*5)*5 = 1 + 1*5 + 1*5^2 + 1*5^3
    A to E 1 + ((1+(1+5)*5)*5)*5 = 1 + 1*5 + 1*5^2 + 1*5^3 + 1*5^4
    a(r^n - 1) / (r - 1) = 1(5^5-1)/(5-1) = 781
    """
    answer = 0
    ex = list(range(1,6))[::-1]
    for i, c in zip(ex, word):
        answer += (pow(5, i) - 1) / (5 - 1) * "AEIOU".index(c) + 1
        #print(c, answer)
        
    return answer















# 풀이 https://leedakyeong.tistory.com/m/entry/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%97%B0%EC%8A%B5-%EC%99%84%EC%A0%84%ED%83%90%EC%83%89-%EB%AA%A8%EC%9D%8C%EC%82%AC%EC%A0%84
# 등비수열 수식 https://ko.wikipedia.org/wiki/%EB%93%B1%EB%B9%84%EC%88%98%EC%97%B4
#def solution(word):
#    answer = 0
#    for i, n in enumerate(word):
#        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
#        # 풀이 https://msiqoc.tistory.com/31
#        # AAAA와 AAAE의 차이는 1*5 + 1 = 6.
#        # AAA와 AAE의 차이는 6*5 + 1 = 31.
#        # AA와 AE의 차이는 31*5 + 1 = 156.
#        # A와 E의 차이는 156*5 + 1 = 781.
#        # A와 E의 차이는 (((1*5 + 1)*5 + 1)*5 + 1)*5 + 1 = 781
#        # A와 E의 차이는 1*5*5*5*5 + 1*5*5*5 + 1*5*5 + 1*5 + 1 = 781
#        # A와 E의 차이는 a*r^4 + a*r^3 + a*r^2 + a*r^1 + a = 781
#        # A와 E의 차이는 a*r^(n-1) + a*r^3) + a*r^2 + a*r^1 + a = 781
#        # A와 E의 차이는 (r^n-1)/(r-1) = (5^5-1)/(5-1) = 781
#        # AA와 AE의 차이는 (5^4-1)/(5-1) = 156
#        # ... 이라서, 자릿수 별로 등비수열로 풀고, 각 자릿수 별로 더하는 것이 위에 수식
#    return answer

# 240201
#def solution(word):
#    answer = 0
#    # AAAA 와 AAAE 의 차이: AAAA, AAAAA, AAAAE, AAAAI, AAAAO, AAAAU, AAAE -> 6
#    # AAA 와 AAE 의 차이: 6*5 + 1 = 31
#    # AA 와 AE 의 차이: 31*5 + 1 = 156
#    # A 와 E 의 차이: 156*5 + 1 = 781
#    # A 와 E 의 차이: ((6*5 + 1)*5 + 1)*5 + 1 = 781
#    # A 와 E 의 차이: 1*5*5*5*5 +1*5*5*5 + 1*5*5 + 1*5 + 1 = 781
#    # A 와 E 의 차이: 1*(5^5-1)/(5-1) = 781
#    for i, c in enumerate(word):
#        answer += 1*(5**(5-i) - 1)/(5-1) * "AEIOU".index(c) + 1 # NOTE 틀린 부분. 마지막 +1 은 A, AA, AAA, AAAA, AAAAE 와 같이 한 글자 늘어날때마다 1씩 늘려야 하기 때문에 붙임
#        
#    return answer

