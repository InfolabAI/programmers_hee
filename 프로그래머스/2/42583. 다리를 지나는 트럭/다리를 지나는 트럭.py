#def solution(bridge_length, weight, truck_weights):
#    return 0
# 240207 정답. 너무 느림. NOTE 차가 이동하는 것을 for 문으로 다루지 말고 list 로 다뤄서 while 내부 for 를 없애자
from collections import deque
def solution(bridge_length, weight, truck_weights):
    queue = deque([[0, bridge_length]])
    cnt = 0
    while queue:
        if queue[0][1] >= bridge_length:
            truck, time = queue.popleft()
        if len(truck_weights) != 0:
            if len(queue) < bridge_length and sum([w for w, t in queue]) + truck_weights[0] <= weight:
                queue.append([truck_weights[0], 0])
                truck_weights = truck_weights[1:]
            
        for i in range(len(queue)):
            queue[i][1] += 1
            
        cnt += 1
        #print(cnt, queue)
    return cnt











#from collections import deque
#def solution(bridge_length, weight, truck_weights):
#    
#    time = 0
#    bridge = deque([0] * bridge_length)
#    truck_weights = deque(truck_weights)
#    
#    currentWeight = 0
#    while len(truck_weights)!=0:
#        time+=1
#
#        currentWeight -= bridge.popleft()
#
#        if currentWeight + truck_weights[0] <= weight:
#            currentWeight+= truck_weights[0]
#            bridge.append(truck_weights.popleft())
#
#        else: 
#            bridge.append(0)
#            
#    time += bridge_length
#    
#    return time

# 231213
#from collections import deque
#def solution(bridge_length, weight, truck_weights):
#    answer = 0
#    bridge = deque([0] * bridge_length) # bridge length 만큼 0 으로 채워져 있고, truck 이 지나가는 부분만 truck weight 로 표현한다고 생각
#    truck_weights = deque(truck_weights)
#    
#    i = 0
#    cur_weight = 0
#    while len(truck_weights) != 0: # 한 턴 마다 bridge 에서 하나가 빠지고, truck 또는 0 이 채워짐
#        passed_truck = bridge.popleft()
#        cur_weight -= passed_truck
#        if cur_weight + truck_weights[0] <= weight:
#            bridge.append(truck_weights[0])
#            cur_weight += truck_weights[0]
#            truck_weights.popleft()
#        else:
#            bridge.append(0)
#        i += 1
#        #print(i, passed_truck, bridge, truck_weights)
#        
#    return i + bridge_length

