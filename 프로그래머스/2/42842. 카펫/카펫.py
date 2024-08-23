#def solution(brown, yellow):
#    return

# 240503
def solution(brown, yellow):
    h = 3
    w = 10000
    while h <= w: # Anki NOTE. brown 을 기준으로 하니 더 간결해짐. 그러나, yellow 를 기준으로 한 코드가 속도 더 빠름.
        if (brown - h*2) % 2 == 0:
            w = (brown - h*2) // 2 + 2 # 현재 h 에 대해 brown 이 사각형을 만들 수 있다면 h, w 를 구함
            if yellow == h*w - brown: # yellow 는 전체 - brown 임
                return [w, h]
        h += 1
    return























# 240314
#def solution(brown, yellow):
#    for i in range(1, (yellow+1)//2+1): # NOTE 틀린 부분. (yellow+1)//2 로 하면 안됨.
#        if yellow % i == 0:
#            yw, yh = i, yellow //i
#            if yh * 2 + yw * 2 + 4 == brown:
#                return [yh+2, yw+2]
#    return -1



#def solution(brown, yellow):
#    for i in range(1, yellow+1):
#        if yellow % i == 0:
#            yw, yh = yellow // i, i
#            if 2*yw + 2*yh + 4 == brown:
#                return yw+2, yh+2

#def solution(brown, yellow):
#    answer = []
#    yellow_x = 0
#    yellow_y = 0
#    for i in range(1, yellow+1):
#        if yellow % i == 0:
#            yellow_x = yellow // i
#            yellow_y = i
#            if 2*yellow_x + 2*yellow_y + 4 == brown:
#                answer.append(yellow_x+2)
#                answer.append(yellow_y+2)
#                break 
#            answer.sort(reverse = True)
#    return answer

