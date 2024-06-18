def solution(stones, k):
    answer = 0
    return answer

def binary_possible(stones, k, mid):
    jumped = 0
    
    for stone in stones:
        if stone < mid:
            jumped += 1
        else:
            jumped = 0
        
        if jumped == k:
            return False
    
    return True

def solution(stones, k):
    answer = 0
    if k == 1:
        return min(stones)
    
    left = min(stones)
    right = max(stones)
    
    while (left < right - 1):
        
        mid = (left + right) // 2
        
        if binary_possible(stones, k, mid):
            left = mid
        else:
            right = mid
    
    answer = left
    

    
    return answer