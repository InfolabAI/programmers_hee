#def solution(numbers, target):
#    return
# 정답
from itertools import product
def solution(numbers, target):
    answer = 0
    for case in list(product(*[(n, -n) for n in numbers])):
        if sum(case) == target:
            answer += 1
        
    return answer




















#from itertools import product
#def solution(numbers, target):
#    p = [(+n, -n) for n in numbers]
#    prod_numbers = map(sum, product(*p))
#    return list(prod_numbers).count(target)
    
#from itertools import product
#from collections import Counter
#def solution(numbers, target):
#    cases = map(sum, product(*[(+n, -n) for n in numbers]))
#    return Counter(cases)[target]

