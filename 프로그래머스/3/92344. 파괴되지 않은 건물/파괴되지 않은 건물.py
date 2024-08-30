#def solution(board, skill):
#    answer = 0
#    return answer



# ref 출처: https://dhalsdl12.tistory.com/24
def solution(board, skill):
    answer = 0
    tmp = [[0 for j in range(len(board[0]) + 1)] for i in range(len(board) + 1)]
    for t, a, b, c, d, degree in skill:
        if t == 2:
            degree = -degree
        tmp[a][b] -= degree
        tmp[a][d+1] += degree
        tmp[c+1][b] += degree
        tmp[c+1][d+1] -= degree
        
    for i in range(len(tmp) - 1):
        for j in range(len(tmp[0]) - 1):
            tmp[i][j+1] += tmp[i][j]
    for i in range(len(tmp) - 1):
        for j in range(len(tmp[0]) - 1):
            tmp[i+1][j] += tmp[i][j]
            
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + tmp[i][j] > 0:
                answer += 1
                
    return answer