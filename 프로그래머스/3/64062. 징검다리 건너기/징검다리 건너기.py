def solution(stones, k):
    answer = 0
    return answer


# 240621
def possible(stones, k, md):
    jumped = 0
    for s in stones:
        if s <= md:
            jumped+=1
        else:
            jumped = 0
       	if jumped >= k:
            #print(f"j {jumped}", end=" ")
            return False
    return True
    
def solution(stones, k):
    answer = 0
    mn, md, mx = 0, 0, max(stones)
    while mn < mx:
        # NOTE 틀린 부분. 어떻게 기준을 계산해야 할지 모르겠음.
        md = (mx+mn)//2
        #print(mn, md, mx, end=' ')
        if possible(stones, k, md):
            mn = md + 1
            #print(f"mn up {mn}")
            answer = mn
        else:
            mx = md
            #print(f"mx dw {mx}")
            answer = mx
    
    #print(mn, md, mx)
    return answer


#ref
#def binary_possible(stones, k, mid):
#    jumped = 0
#    
#    for stone in stones:
#        if stone < mid:
#            jumped += 1
#        else:
#            jumped = 0
#        
#        if jumped == k:
#            return False
#    
#    return True
#
#def solution(stones, k):
#    answer = 0
#    if k == 1:
#        return min(stones)
#    
#    left = min(stones)
#    right = max(stones)
#    
#    while (left < right - 1):
#        
#        mid = (left + right) // 2
#        
#        if binary_possible(stones, k, mid):
#            left = mid
#        else:
#            right = mid
#    
#    answer = left
#    
#
#    
#    return answer


# 240618
# 정답은 맞지만 효율성 통과 못함. 모든 디딤돌의 수를 하나씩 빼면서 가장 긴 공백을 찾다가 그 값이 k 보다 커지면 answer.
#def find_longest_space(stones):
#    longest_len = 0
#    len = 0
#    for s in [9e+20] + stones + [9e+20]:
#        if s == 0:
#            len += 1
#        else:
#            if len > longest_len:
#                longest_len = len
#            len = 0
#    return longest_len
#
#def solution(stones, k):
#    answer = 1
#    while True:
#        new_stones = []
#        
#        for s in stones:
#            new_stones.append(s if s == 0 else s-1)
#        
#        l = find_longest_space(new_stones)
#        
#        #print(new_stones, l, answer)
#        if l >= k:
#            answer+=1
#            break
#        
#        stones = new_stones
#        answer+=1
#
#    return answer-1