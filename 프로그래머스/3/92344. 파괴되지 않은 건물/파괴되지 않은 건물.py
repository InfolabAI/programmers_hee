def solution(board, skill):
    tmp = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    
    for t, r1, c1, r2, c2, d in skill:
        if t == 1:
            d = -d
        tmp[r1][c1] += d
        tmp[r2+1][c2+1] += d
        tmp[r1][c2+1] -= d
        tmp[r2+1][c1] -= d
    
    for r in range(len(tmp)-1):
        for c in range(len(tmp[0])):
            tmp[r+1][c] += tmp[r][c]
            
    for r in range(len(tmp)):
        for c in range(len(tmp[0])-1):
            tmp[r][c+1] += tmp[r][c]
            
    for r in range(len(tmp)-1):
        for c in range(len(tmp[0])-1):
            board[r][c] += tmp[r][c]
    
    total = 0
    for r in range(len(tmp)-1):
        for c in range(len(tmp[0])-1):
            if board[r][c] >= 1:
                total += 1
    
    return total

# NOTE 틀린 부분. skill 이 아니라, r, c 를 기준으로 해도 시간초과 발생
#import numpy as np
#def solution(board, skill):
#    answer = 0
#    degreem = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
#    for c in range(len(board[0])):
#        for r in range(len(board)):
#            for t, r1, c1, r2, c2, degree in skill:
#                if r1 <= r and r <= r2 and c1 <= c and c <= c2:
#                    degreem[r][c] = degreem[r][c] + (degree if t == 2 else -degree)
#    return
    
# 240830
# NOTE 틀린 부분. numpy 사용해도 효율성 테스트 통과 안됨, 효율성을 의해 DP 를 써야함
#import numpy as np
#def solution(board, skill):
#    answer = 0
#    board = np.array(board)
#    for t, r1, c1, r2, c2, degree in skill:
#        r2, c2 = r2+1, c2+1
#        if t == 1:
#            board[r1:r2, c1:c2] -= degree
#        else:
#            board[r1:r2, c1:c2] += degree
#    #for row in board:
#    #    print(row)
#    
#    return (board>0).sum().item()



# ref 출처: https://dhalsdl12.tistory.com/24
#def solution(board, skill):
#    answer = 0
#    tmp = [[0 for j in range(len(board[0]) + 1)] for i in range(len(board) + 1)]
#    for t, a, b, c, d, degree in skill:
#        if t == 2:
#            degree = -degree
#        tmp[a][b] -= degree
#        tmp[a][d+1] += degree
#        tmp[c+1][b] += degree
#        tmp[c+1][d+1] -= degree
#        
#    for i in range(len(tmp) - 1):
#        for j in range(len(tmp[0]) - 1):
#            tmp[i][j+1] += tmp[i][j]
#    for i in range(len(tmp) - 1):
#        for j in range(len(tmp[0]) - 1):
#            tmp[i+1][j] += tmp[i][j]
#            
#    for i in range(len(board)):
#        for j in range(len(board[0])):
#            if board[i][j] + tmp[i][j] > 0:
#                answer += 1
#                
#    return answer