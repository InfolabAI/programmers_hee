#def solution(m, n, puddles):
#    return 0
# 240313
import numpy as np
def printm(map):
    print()
    for row in map:
        print(row)
def solution(m, n, puddles):
    #map = np.zeros((n+1, m+1)) # NOTE 틀린 부분. list 가 빠름.
    #map = [[0] * (m+1)] * (n+1) # NOTE 틀린 부분. list 을 이렇게 초기화 하면 [1][1] 로 접근해서 값 넣는게 실패. 한 열단위로만 넣어짐.
    map = [[0] * (m+1) for _ in range(n+1)]
    for c, r in puddles: # NOTE 틀린 부분. 순서 또 틀림.
        map[r][c] = -1
    map[1][1] = 1
    for r in range(1,n+1):
        for c in range(1,m+1):
            if (r,c) == (1,1):
                continue
            if map[r][c] == -1:
                map[r][c] = 0
            elif map[r][c] == 0:
                map[r][c] += (map[r-1][c]+map[r][c-1])
                
    #printm(map)
    
    return map[-1][-1] % 1000000007
    
    
    
    
    
    
    
    
    
    
    
    
    














# Reinforcement learning 
#def solution(m, n, puddles):
#    A = [[0] * (m+1) for _ in range(n+1)]
#    A[1][1] = 1				# 시작 위치 표시
#    
#    for pr, pc in puddles:	# 물 웅덩이 표시
#        A[pc][pr] = -1
#
#    for r in range(1, n+1):
#        for c in range(1, m+1):
#            if (r, c) == (1, 1):	# 시작 위치는 무시
#                continue
#            if A[r][c] == -1:		# 물 웅덩이면 0으로 바꿔줌
#                A[r][c] = 0
#            else:
#                A[r][c] += (A[r-1][c] + A[r][c-1])	# 좌, 상 방향의 값을 더해줌
#    
#    #for a in A:
#    #    print(a)
#        
#    return A[n][m] % 1000000007

# 240311
#import numpy as np
#def solution(m, n, puddles):
#    #map = np.zeros((n+1, m+1), dtype=np.int16) # NOTE 틀린 부분. map 을 numpy array 로 사용하면, 효율성 테스트 실패. 그렇다고 np.int16 과 같이 줄이면, 경우의 수를 모두 담지 못해 실패. list 로 해야 효율성 테스트 성공.
#    map = [[0] * (m+1) for _ in range(n+1)]
#    map[1][1] = 1
#    for x, y in puddles:
#        map[y][x] = -1 # NOTE 틀린 부분. y 가 앞이고, x 가 뒤임
#        
#    for x in range(1,n+1):
#        for y in range(1,m+1):
#            if (x, y) == (1, 1):
#                continue
#            if map[x][y] == -1:
#                map[x][y] = 0
#            else:
#                map[x][y] += (map[x-1][y] + map[x][y-1])
#                
#    
#    return int(map[n][m] % 1000000007)

