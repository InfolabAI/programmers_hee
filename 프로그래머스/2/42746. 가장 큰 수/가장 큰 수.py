#def solution(numbers):
#    return
# 240327
def solution(numbers):
    # 맨 앞자리에 갔을때 가장 클 수부터
    sorted_numbers = sorted([(str(n)*3, i) for i, n in enumerate(numbers)], key=lambda x:x[0], reverse=True)
    # sorted_numbers == [('666', 0), ('222', 2), ('101010', 1)]
    answer = []
    for nnn, i in sorted_numbers:
        answer.append(str(numbers[i]))
    
    return str(int("".join(answer))) # NOTE str 자체로 return 하면 case 11 실패, int 로 바꿨다가 str 로 다시 바꾸면 모두 정답. "00000" 같은 숫자는 실패하나 봄.












#def solution(numbers):
#    numbers = list(map(str, numbers))
#    numbers.sort(key=lambda x: x*3, reverse=True)
#    return str(int(''.join(numbers)))

#def solution(numbers):
#    ret = sorted([str(n) for n in numbers], key=lambda x:x*3, reverse=True)
#    return str(int(''.join(ret)))

#240327 시간 초과 코드.
#from itertools import permutations, combinations
#def solution(numbers):
#    numbers = [str(n) for n in numbers]
#    maxn = ""
#    for number in combinations(numbers, len(numbers)): # NOTE 틀린 부분. permutations 를 쓰면, 정답은 맞지만 시간 초과, combinations 를 쓰면, 틀림.
#        number = "".join(number)
#        if number > maxn:
#            maxn = number
#        #print(maxn, number)
#    return maxn




