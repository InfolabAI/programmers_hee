def solution(a):
    answer = 0
    return answer

# 240822
# 최후까지 남은 풍선이 시작점
# 만약 작은 풍선 터뜨리는 기회가 1번도 없다면, 가작 번호가 작은 풍선만 남게됨
# NOTE 틀린 부분. 이 공식을 생각하지 못함. 공식: 만약 작은 풍선 터뜨리는 기회가 1번이라면, left 최소값, right 최소값 둘 다 기준 풍선보다 작은게 아니라면 기준 풍선은 남을 수 있음
def solution(a):
    answer = 0
    # NOTE 틀린 부분. 정답이지만, 시간초과. minmax 를 사전에 for 문 1번으로 구해놓고 사용해야 함.
    #for i in range(len(a)):
    #    left = a[:i] if len(a[:i]) != 0 else [1000000001]
    #    right = a[i+1:] if len(a[i+1:]) != 0 else [1000000001]
    #    #print(left, right)
    #    if a[i] > min(left) and a[i] > min(right):
    #        continue
    #    else:
    #        answer += 1
    
    leftmin, rightmin = a[0], a[-1]
    minmax = [[0, el, 0] for el in a]
    for l, r in zip(range(len(a)), reversed(range(len(a)))):
        # 특정 시점에서 가장 작은 수를 누적 게산
        leftmin = a[l] if a[l] < leftmin else leftmin
        rightmin = a[r] if a[r] < rightmin else rightmin
        minmax[l][0] = leftmin
        minmax[r][2] = rightmin
        
    for l, m, r in minmax:
        if l < m and r < m:
            continue
        else:
            answer += 1
        
    return answer

# ref https://tiktaek.tistory.com/m/64
#def solution(a):
#    answer = 0
#    alen = len(a)
#    left, right = a[0], a[-1]
#    minmax = [[0, ele, 0] for ele in a]     # 왼쪽 최소, a원소, 오른쪽 최소
#    for l, r in zip(range(alen), range(len(a) - 1, -1, -1)):
#        if left > a[l]:
#            left = a[l]
#        if right > a[r]:
#            right = a[r]
#        minmax[l][0] = left
#        minmax[r][2] = right
#
#    for idx in range(alen):                 # 왼쪽 최소와 오른쪽 최소 중에서
#        left, mid, right = minmax[idx]      # a의 원소보다 큰수가 하나이하 일때
#        if left < mid and right < mid:
#            continue
#        answer += 1
#
#    return answer