#def solution(brown, yellow):
#    return
# 240314
def solution(brown, yellow):
    for i in range(1, (yellow+1)//2+1): # NOTE 틀린 부분. (yellow+1)//2 로 하면 안됨.
        if yellow % i == 0:
            yw, yh = i, yellow //i
            if yh * 2 + yw * 2 + 4 == brown:
                return [yh+2, yw+2]
    return -1





















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

