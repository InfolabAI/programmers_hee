# 240808
def get_palindrome_odd(s, i):
    offset = 0
    p, n, pp, nn = i, i, i, i
    while p>=0 and n<len(s) and s[p] == s[n]: # NOTE 틀린부분. 이렇게하면 펠린드롬이 홀수일때만 찾을 수 있음.
        offset += 1
        pp, nn = p, n
        p, n = i-offset, i+offset
    subset = s[pp:nn+1]
    #print("odd", offset, subset, end=" ")
    return (offset-1)*2+1, subset

def get_palindrome_even(s, i):
    offset = 0
    p, n, pp, nn = i, i+1, i, i+1
    #print(p, n, s[p:n+1], end=" > ")
    while p>=0 and n<len(s) and s[p] == s[n]: 
        offset += 1
        pp, nn = p, n
        p, n = i-offset, i+1+offset
        #print(p, n, s[p:n+1], offset, end=" > ")
    subset = s[pp:nn]
    #print("even", offset, subset)
    #print()
    return offset*2, subset
    
def solution(s):
    mx = 0
    for i in range(len(s)):
        oddmx = get_palindrome_odd(s, i)[0]
        evenmx = get_palindrome_even(s, i)[0]
        curmx = max(oddmx, evenmx)
        if mx < curmx:
            mx = curmx
    return mx