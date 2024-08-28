def solution(n, s, a, b, fares):
    answer = 0
    return answer

# ref   출처: https://nauco.tistory.com/48 [UNDERSTANDING:티스토리]
def solution(n, s, a, b, fares):
    answer = n*1000001
    d = [[n*100001]*n for _ in range(n)]
        
    for k in range(n):
        d[k][k] = 0
        
    for fare in fares:
        x, y, f = fare
        d[x-1][y-1] = f
        d[y-1][x-1] = f

        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    
    for k in range(n):
        answer = min(answer, d[s-1][k] + d[k][a-1] + d[k][b-1]) 
    return answer