#def solution(nbs):
#    return
# 240318 최대 2500ms. NOTE 트린부분
from itertools import permutations as pt
def solution(nbs):
    cases = set()
    for i in range(1, len(nbs) + 1): # NOTE. 초기화를 바꿔서는 속도 개선 없음
        cases |= set(int("".join(c)) for c in pt(nbs, i))
    a = cases
    
    max_iter = int(max(a)**0.5) + 1 # NOTE. 이전 버전 최대 2500ms
    max_nbs = max(a)
    a -= set([0, 1])
    for i in range(2, max_iter):
        #diff = set(n for n in range(i*2, max_nbs+1, i))
        diff = set(range(i*2, max(a)+1, i)) # NOTE. 여기가 문제였음. max_nbs 를 쓰면 느리고, max(a) 를 쓰면 빠름. 매번 a 의 max 를 구하는데 왜?. 아.. a 는 계속 바뀌고 a 의 max 가 작아질 수 있음. max_nbs 를 쓰면 불필요한 iteration 을 도는 것.
        a -= diff
        
    #a -= set([0, 1])  # NOTE. 여기를 바꿨더니 속도 개선이 있음. # NOTE. 개선 버전 최대 1000ms. 완전히 같은 코드인데 뭐가 문제지?
    #max_ = int(max(a)**0.5)+1
    #for n in range(2, max_):
    #    diff = set(range(n*2, max(a) + 1, n))
    #    a -= diff
    #    #print(f"diff {diff} \na {a}")
        
    return len(a)
















#from itertools import permutations
#def solution(n):
#    a = set()
#    for i in range(len(n)):
#        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#    
#    #print(a)
#    # 0, 1 은 처음부터 배제함
#    a -= set(range(0, 2))
#    #print(a)
#    # 최고값의 root 까지만 돌면되기 때문에 ** 0.5
#    for i in range(2, int(max(a) ** 0.5) + 1):
#        # 에라토스테네스의 체는 자신은 빼면 안되기 때문에, i*2 가 시작.
#        # 배수들을 빼야 하므로, range(,,i)
#        a -= set(range(i * 2, max(a) + 1, i))
#        #print(i, sorted(list(set(range(i * 2, max(a) + 1, i)))))
#    return len(a)

# someday 최대 1000ms
#from itertools import permutations
#def solution(numbers):
#    a = set()
#    for i in range(1, len(numbers)+1):
#        a |= set([int(''.join(p)) for p in permutations([n for n in numbers], i)])
#    #print(a)
#    
#    a -= set([0, 1])
#    max_ = int(max(a)**0.5)+1
#    for n in range(2, max_):
#        diff = set(range(n*2, max(a) + 1, n))
#        a -= diff
#        #print(f"diff {diff} \na {a}")
#        
#    return len(a)


# 240315
#from collections import deque
#from itertools import permutations as pm # NOTE 틀린 부분. 모든 경우의 수를 만드는 방법.
#def solution(numbers):
#    all_case_numbers = []
#    for i in range(1, len(numbers)+1):
#        for case in pm(numbers, i): # NOTE 틀린 부분. [1, 7] 로는 [1, 7, 17, 71] 총 4가지가 있는데, [17, 71] 만 고려하는 문제가 있었음.
#            all_case_numbers.append(int(''.join(case)))
#            
#    set_n = set(all_case_numbers)
#    set_n -= {0, 1}
#    for n in range(2, int(max(set_n)**0.5)+1):
#        diff = set(range(n*2, max(set_n)+1, n))
#        set_n -= diff
#        #print(diff, set_n)
#        pass
#    
#    #print(set_n)
#    #sosu = [i for i in range(2, max(set_n)+1)] # NOTE 틀린 부분. 에라토스테네스의 채 를 구하는 개발.
#    #print(set_n, sosu)
#    return len(set_n)

