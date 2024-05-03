#def solution(name):
#    return 0
# 240223
def solution(name):
    answer = 100000
    if set(name) == {'A'}: # NOTE 틀린, 오래 걸린 부분
        return 0
    
    for i in range(len(name)//2 + 1):
        l_r = name[-i:] + name[:-i]
        #print(l_r)
        r_l = name[i::-1] + name[:i:-1]
        #print(r_l)
        for line in [l_r, r_l]:
            while line and line[-1] == 'A':
                line = line[:-1]
            cnt = sum([ min(ord(c) - ord('A'), ord('Z') + 1 - ord(c)) for c in line ])
            answer = min(answer, cnt + i - 1 + len(line)) # NOTE 틀린, 오래 걸린 부분
            #print(i, line, cnt, answer)
        
    return answer

















#def solution(name):
## 두번 꺽는 경우는 고려하지 않음
#
#    if set(name) == {'A'}:
#        return 0
#
#    a_pos = ord('A') # 'A' : 65, 'Z' : 90
#    z_pos = ord('Z')
#
#    answer = float('inf')
#
#    print(name, f"{name[0]} 에서 시작")
#    for i in range(len(name)//2 + 1):
#        l_r = name[-i:] + name[:-i] 
#        print(f"\n좌측으로 [{i}]번 간 후, 우측으로 주욱 가는 것 l_r {name[-i:]}, {name[:-i]}")
#        
#        r_l = name[i: :-1] + name[i+1:][::-1] 
#        print(f"우측으로 [{i}]번 간 후, 좌측으로 주욱 가는 것 r_l {name[i: :-1]}, {name[i+1:][::-1]}")
#        
#        for n in [l_r,r_l]:
#            # 끝에 A들은 셀 필요 없으므로 자르기
#            while n and n[-1] == 'A':
#                n = n[:-1]
#            cnt = [min(ord(c)-a_pos, (z_pos+1) - ord(c)) for c in n ] # A 를 제외한 후의 A부터의 거리와 Z부터의 거리의 min 을 모음
#            answer = min(answer, i + (len(cnt)-1) + sum(cnt)) # 어느 위치에서 움직이는 것이 좋은지 min 값을 계속 누적
#
#    return answer

# 240111 버전
#def solution(name):
#    if set(name) == {'A'}:
#        return 0
#    answer = 1e+10 
#    for i in range(len(name)//2 + 1):
#        lr1 = name[-i:]
#        lr2 = name[:-i]
#        rl1 = name[i::-1]
#        rl2 = name[:i:-1]
#        #print(f"{i}: {lr1}+{lr2} {rl1}+{rl2}")
#        
#        for n in [lr1+lr2, rl1+rl2]:
#            while n and n[-1] == 'A':
#                n = n[:-1]
#            cnt=0
#            for c in n:
#                cnt += min(ord(c) - ord('A'), ord('Z')+1 - ord(c)) # 이해 안되는 부분. 여기 왜 +1 이 필요하지?
#            answer = min(answer, i + len(n) + cnt -1) # 이해 안되는 부분. 여기 왜 -1 이 필요하지?
#    return answer


# 240110 시도 버전

#def solution(name):
#    answer = 100000000
#    
#    if set(name) == {'A'}: # 틀린 부분
#        return 0
#    
#    for i in range(len(name)//2+1):
#        lr1 = name[-i:]
#        lr2 = name[:-i]
#        rl1 = name[i::-1]
#        rl2 = name[:i:-1]
#        lr, rl = lr1+lr2, rl1+rl2
#        #print(f"{i}. {lr1}+{lr2} {rl1}+{rl2}")
#        
#        for n in [lr, rl]:
#            while n and n[-1]=='A':
#                n = n[:-1]
#            cnt = 0
#            for c in n:
#                cnt += min(ord(c) - ord('A'), ord('Z') + 1 - ord(c)) # 틀린 부분
#            answer = min(answer, i + cnt + len(n) -1) # 틀린 부분
#    return answer



# 240109 시도 버전

#def solution(name):
#    if set(name) == {'A'}: # 틀린 부분
#        return 0
#    
#    answer = 10000000
#    print(name)
#    for i in range(len(name)//2 + 1): # 틀린 부분
#        l_r1 = name[-i:]
#        l_r2 = name[:-i]
#        print(f"\nl_r {l_r1} + {l_r2}")
#        l_r = l_r1 + l_r2
#        r_l1 = name[i::-1]
#        r_l2 = name[:i:-1]
#        r_l = r_l1 + r_l2
#        print(f"r_l {r_l1} + {r_l2}")
#        
#        for n in [l_r, r_l]:
#            while n and n[-1] == 'A':
#                n = n[:-1]
#            cnt = [min(ord(c) - ord('A'), ord('Z')+1 - ord(c)) for c in n] # 틀린 부분
#            answer = min(answer, i + sum(cnt)-1 + len(n)) # 틀린 부분
#    
#    return answer

# 240221 DFS 로는 불가능함을 깨달은 버전. 일부 통과하나 길이가 길면 매우 느림. 성공은 했던 버전이었는데, 마구 고치다가 지금은 버그만 남은 버전.
#from collections import deque
#import numpy as np
#def DFS(graph, visited):
#    stack = deque([(0, 0)])
#    i = 0
#    while stack:
#        pos, dist = stack.pop()
#        graph[pos] == 0
#        print(pos, dist, visited)
#        i = i + 1
#        if i > 2:
#            break
#        if sum(graph) == 0:
#            break
#        for i in range(len(graph)//2+1):
#            n1_pos = pos + i
#            if n1_pos >= len(graph):
#                n1_pos = n1_pos - len(graph)
#            n2_pos = pos - i
#            if n2_pos < 0:
#                n2_pos = n2_pos + len(graph) - 1
#            if graph[n1_pos] == 1:
#                stack.append((n1_pos, dist+1))
#                break
#            if graph[n2_pos] == 1:
#                stack.append((n2_pos, dist+1))
#                break
#    return dist
#        
#def solution(name):
#    a0 = abs(ord('A') - ord(name[0]))
#    graph = np.array(list(map(lambda x:int(x!='A'), name)))
#    #visited = np.array(list(map(lambda x:int(x!='A'), name)))
#    #total = 0
#    #for c in name:
#    #    total += min(abs(ord('A') - ord(c)), abs(ord('Z') - ord(c) + 1))
#    moves = DFS(graph, None)
#    #return total + moves
#    return

