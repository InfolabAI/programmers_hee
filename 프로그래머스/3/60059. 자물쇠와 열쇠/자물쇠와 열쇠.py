def printm(m):
    for row in m:
        print(row)
        
import numpy as np

# 240827
# 열쇠 회전가능, 이동가능, 열쇠가 map 을 벗어나도 됨
# NOTE 틀린 부분. key 의 이동, key 가 가져진 경우의 수를 어떻게 계산할 것인가?. 답: key 양옆위아래에 lcok 만큼의 map 을 더 만들어서 lock 을 움직이면서 비교하면 됨
def solution(key, lock):
    answer = True
    key, lock = np.array(key), np.array(lock)
    keylen, locklen = len(key), len(lock)
    
    # lock 반전
    lock_tmp = lock - 1
    lock_tmp[lock_tmp==-1] = 1
    
    for i in range(4):
        # key 확장
        # key 와 lock 은 최소 1행열은 겹쳐야 하므로, locklen-1
        exkey = np.array([[0 for _ in range(2*(locklen-1)+keylen)] for _ in range(2*(locklen-1)+keylen)])
        exkey[locklen-1:locklen-1+keylen, locklen-1:locklen-1+keylen] = key

        for r in range(len(exkey)-locklen+1): # NOTE 틀린 부분. keylen 을 기준으로 이동하면 에러남. lock 을 움직이므는게 목적인데, lock 이 key 보다 큰 경우면 범위를 벗어나기 때문. locklen 기준으로 수행해야 함.
            for l in range(len(exkey)-locklen+1):
                key_tmp = exkey[r:r+locklen, l:l+locklen]
                #printm(key_tmp)
                if (key_tmp == lock_tmp).all():
                    return True
        key = np.rot90(key, k=1) # NOTE 틀린 부분. k=i 이면 틀림. 누적이므로 매번 1만큼 돌려야 함.
    
    return False

#def rotate(board, key_len): #열쇠 시계방향으로 90도 회전
#    tmp = [[0 for _ in range(key_len)] for _ in range(key_len)]
#    for i in range(key_len):
#        for j in range(key_len):
#            tmp[j][key_len - i - 1] = board[i][j]
#    return tmp
#
#
#def check(key, lock, key_len, lock_len):
#    arr = [[0 for _ in range(2 * (lock_len - 1) + key_len)] for _ in range(2 * (lock_len - 1) + key_len)]
#    
#    #열쇠를 자물쇠의 크기만큼 확장
#    for i in range(key_len): 
#        for j in range(key_len):
#            arr[lock_len + i - 1][lock_len + j - 1] = key[i][j]
#    printm(arr)
#    print()
#    printm(key)
#    print()
#    printm(lock)
#    
#    #확장한 열쇠에서 왼쪽 위의 자표를 (0,0)부터 (key_len + lock_len -1, key_len + lock_len -1)까지 탐색
#    for a in range(lock_len + key_len - 1):
#        for b in range(lock_len + key_len - 1):
#            check = True
#            for i in range(lock_len):
#                for j in range(lock_len):
#                    check = check and (arr[a + i][b + j] != lock[i][j])
#            if check: #모든 홈이 일치한다면 참값을 반환
#                return True
#
#    return False
#
#
#def solution(key, lock):
#    answer = False
#    key_len = len(key) 
#    lock_len = len(lock)
#    for _ in range(4): # 4번 회전시켜 각 케이스 확인
#        answer = check(key, lock, key_len, lock_len) or answer #모든 모양에 대해 열쇠와 자물쇠의 홈이 일치하는지 확인
#        key = rotate(key, key_len) # 열쇠 회전
#    return answer