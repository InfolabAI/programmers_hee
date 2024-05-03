from collections import deque
def solution(number, k):
    stack = deque([])
    for c in number:
        while k>0 and stack and stack[-1] < c:
            poped = stack.pop()
            #print(f"{number}, poped {poped}")
            k -= 1
        stack.append(c)
    return "".join(stack)[:len(number) - k]
        

















# https://chiefcoder.tistory.com/37
#def solution(number, k):
#    answer = []
#
#    for i in number:
#        while k > 0 and answer and answer[-1] < i: # 바로 이전 숫자보다 숫자가 크면 이보다 작은 수부터 순서대로 k 만큼 pop. stack 이라 작은 수부터 빠짐.
#            poped = answer.pop()
#            k -= 1
#            print('at', i, 'pop', poped, answer)
#        answer.append(i)
#        print('append', answer)
#
#    return ''.join(answer[:len(answer) - k])

# 240115 버전
#def solution(number, k):
#    answer = []
#    for c in number:
#        while answer and c > answer[-1] and k > 0: # 틀린 부분
#            k -= 1
#            answer.pop()
#        answer.append(c)
#    
#    return "".join(answer[:len(number) - k])

# 240112 버전
#from collections import deque
#def solution(number, k):
#    answer = deque([])
#    for c in number:
#        while k > 0 and len(answer) > 0 and answer[-1] < c: # 틀린 부분
#            answer.pop()
#            k -= 1
#        answer.append(c)
#    return "".join(answer)[:len(number) - k] # 틀린 부분. 위 for 문을 돌았다고 해서 answer 가 len(number) - k 를 보장하지는 않음.
#	# return answer # JSON error. deque 는 print 가 안 됨.

# 240116
#from collections import deque
#def solution(number, k):
#    answer = deque([])
#    for c in number:
#        while answer and c > answer[-1] and k > 0:
#            answer.pop()
#            k -= 1
#        answer.append(c)
#        
#    return "".join(answer)[:len(number) - k]

# 240223
#from collections import deque
#def solution(number, k):
#    stack = deque([])
#    for n in number:
#        while stack and k > 0 and stack[-1] < n: 
#            poped = stack.pop() # NOTE 틀린 부분
#            #print(f"at {n} pop {poped} > {stack}")
#            k -= 1
#        stack.append(n)
#        #print(f"append {n}")
#            
#    return "".join(stack)[:len(number)-k] # NOTe 틀린 부분. 위에 while 이 k 개가 제외됨을 보장하지는 않음


# 240227
#from collections import deque
#def solution(number, k):
#    stack = deque([])
#    answer = []
#    for c in number:
#        while k > 0 and stack and c > stack[-1]: 
#            # NOTE 틀린 부분. 작은 수를 stack 로 앞에서부터 빼면, 뒤에 작은 수는 어떻게 빼지?
#            # stack 이 맞음. stack 은 만약 [1, 9] 면 9 가 빠지지 않을까? 라는 문제를 고민할 필요가 없음. 왜냐하면, 1 은 이미 9 를 넣기 전에 빠지기 때문.
#            poped = stack.pop()
#            #print(f"pop {poped} k {k}")
#            k -= 1
#        stack.append(c)
#        #print(stack)
#    
#    if k > 0:
#        return "".join(stack)[:-k] # NOTE 틀린 부분. 틀렸다기 보단 비효율. 그냥 len(answer) - k 하면 됨.
#    else:
#        return "".join(stack)