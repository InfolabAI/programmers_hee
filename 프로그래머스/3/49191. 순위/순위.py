#def solution(n, results):
#    return
#240422
from collections import defaultdict
def printmap(adj):
    for row in adj:
        print(row)

def num_zero(row):
    zero = 0
    for c in row:
        if c == 0:
            zero+=1
    return zero

def solution(n, results):
    #adj = [[0]*(n+1)]*(n+1)
    # NOTE 틀린 부분. [0]*n 과 [0 for _ in range(n)] 은 다른 리스트이다. [0]*n 은 하나를 바꾸면 전체가 바뀐다.
    adj = [[0 for _ in range(n)] for _ in range(n)]
    
    # 0: no edge, 1: defeat, 2: win
    for w, l in results:
        w, l = w-1, l-1 # NOTE 틀린 부분. w-1, l-1 을 생각하지 않으면 밑에 3 loop 에서 index 가 안 맞음
        adj[w][l] = 2
        adj[l][w] = 1
        
    #printmap(adj)
    #print()
    for k in range(n):
        for s in range(n):
            for t in range(n):
                if adj[s][k] == 2 and adj[k][t] == 2:
                    adj[s][t] = 2
                    #print(s, t, "w")
                if adj[s][k] == 1 and adj[k][t] == 1:
                    adj[s][t] = 1
                    #print(s, t, "l")

    #printmap(adj)
    
    answer = 0
    for row in adj:
        if num_zero(row) <= 1:
            answer += 1
        
    return answer















#def solution(n, results):
#    # 0: edge 없음. 1: 패배, 2: 승리 3: 자신
#    adjm = [[0 for _ in range(n)] for _ in range(n)]
#    print(adjm)
#    for i in range(n):
#        adjm[i][i] = 3
#    
#    for res in results:
#        # 플로이드-워셜인데 노드 간 edge가 패배 또는 승리 인 것
#        adjm[res[0]-1][res[1]-1] = 2
#        adjm[res[1]-1][res[0]-1] = 1
#    
#    for k in range(n):
#        #중간 노드가 k임
#        for i in range(n):
#            for j in range(n):
#                # 조건 헷갈림. elif 조심.
#                #k를 통했을 때, 두 edge 가 둘 다 '승리'이면, '승리'으로 update
#                if adjm[i][k] == 2 and adjm[k][j] == 2:
#                    adjm[i][j] = 2
#                #k를 통했을 때, 두 edge 가 둘 다 '패배'이면, '패배'으로 update
#                if adjm[i][k] == 1 and adjm[k][j] == 1:
#                    adjm[i][j] = 1
#                    
#                    
#    
#    ans = 0
#    #1개 행에 ?가 한 개도 없으면 순위를 매길 수 있는 선수임
#    for adjl in adjm:
#        if not 0 in adjl:
#            ans += 1
#            
#    return ans
        
    
#def solution(n, results):
#    # 0: edge 없음. 1: 패배, 2: 승리 3: 자신
#    adj_mat = [[0 for _ in range(n)] for _ in range(n)]
#    for i in range(n):
#        adj_mat[i][i] = 3
#    for ret in results:
#        win = ret[0] - 1
#        lose = ret[1] - 1
#        adj_mat[win][lose] = 2
#        adj_mat[lose][win] = 1
#    for k in range(n):
#        for i in range(n):
#            for j in range(n):
#                if adj_mat[i][k] == 2 and adj_mat[k][j] == 2:
#                    adj_mat[i][j] = 2
#                if adj_mat[i][k] == 1 and adj_mat[k][j] == 1:
#                    adj_mat[i][j] = 1
#    ans = 0
#    for i in range(n):
#        if adj_mat[i].count(0) == 0:
#            ans += 1
#    
#    return ans


