def solution(n, s):
    answer = []
    return answer

# ref1
def solution(n, s):
    # 자연수 n개의 합으로 n보다 작은 s를 만들 수는 없으므로 [-1]을 리턴한다
    if n > s: return [-1]
    result = []
    # s를 n으로 나눈 몫이 n개이도록 초기값을 정한다.
    initial = s // n
    for _ in range(n):
        result.append(initial)
    idx = len(result) - 1
    # s를 n으로 나눈 몫에서 나머지만큼 각 값에 1씩 더해준다.
    for _ in range(s % n):
        result[idx] += 1
        idx -=1
    return result

# ref2
def bestSet(n, s):
    answer = []
    a = int(s/n)

    if a == 0:
        return [-1]

    b = s%n

    for i in range(n-b):
        answer.append(a)
    for i in range(b):
        answer.append(a+1)

    return answer
