#def solution(triangle):
#    answer = 0
#    return answer
# 240503
def solution(triangle):
    tt = triangle
    for i, row in enumerate(tt):
        if i == 0:
            continue
        else:
            for j in range(len(row)):
                if j == 0:
                    tt[i][j] += tt[i-1][j]
                elif j == len(row)-1:
                    tt[i][j] += tt[i-1][j-1]
                else:
                    tt[i][j] += max(tt[i-1][j], tt[i-1][j-1])
        
    return max(tt[-1])



















#240311
#def solution(triangle):
#    tt = triangle
#    answer = 0
#    for i in range(len(tt)):
#        if i == 0:
#            continue
#        for j in range(len(tt[i])):
#            if j == 0:
#                tt[i][j] += tt[i-1][j]
#            elif j == len(tt[i])-1:
#                tt[i][j] += tt[i-1][j-1]
#            else:
#                tt[i][j] += max(tt[i-1][j-1] , tt[i-1][j])
#        
#    return max(tt[-1])


#def solution(triangle):
#    answer = 0
#    t = triangle
#    for i, _ in enumerate(t):
#        if i == 0:
#            continue
#        for j in range(i+1):
#            if j == 0:
#                t[i][j] += t[i-1][j]
#            elif j == i:
#                t[i][j] += t[i-1][-1]
#            else:
#                t[i][j] += max(t[i-1][j-1], t[i-1][j])
#        
#    return max(t[-1])
#

