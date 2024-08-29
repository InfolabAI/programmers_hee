def solution(n, source, a, b, fares):
    return
        
# 240829
def solution(n, source, a, b, fares):
    answer = n*1000001 # NOTE 틀린 부분. 100001 은 edge 하나당 최고 비용임. 총 최고비용은 모든 node 를 방문하는 비용임.
    d = [[n*100001 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
        
    for s, t, f in fares:
        s, t = s-1, t-1
        d[s][t] = f
        d[t][s] = f
        
    for k in range(n): # NOTE 틀린 부분. 플로이드-워셜 쓸 생각을 못했음.
        for s in range(n):
            for t in range(n):
                tmp = d[s][k] + d[k][t]
                if tmp < d[s][t]:
                    d[s][t] = tmp
    
    for k in range(n): # NOTE 틀린 부분. 플로이드-워셜 이후, A, B 모두를 최단경로로 이동하는 비용 계산을 하지 못했음.
        answer = min(answer, d[source-1][k] + d[k][a-1] + d[k][b-1])
    return answer

# ref https://nauco.tistory.com/48 [UNDERSTANDING:티스토리]
#def solution(n, s, a, b, fares):
#    answer = n*1000001
#    d = [[n*100001]*n for _ in range(n)]
#        
#    for k in range(n):
#        d[k][k] = 0
#        
#    for fare in fares:
#        x, y, f = fare
#        d[x-1][y-1] = f
#        d[y-1][x-1] = f
#
#        
#    for k in range(n):
#        for i in range(n):
#            for j in range(n):
#                if d[i][k] + d[k][j] < d[i][j]:
#                    d[i][j] = d[i][k] + d[k][j]
#                    
#    for k in range(n):
#        answer = min(answer, d[s-1][k] + d[k][a-1] + d[k][b-1]) 
#    return answeat