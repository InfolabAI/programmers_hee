#def solution(jobs):
#    return
# 240321
from heapq import heappush, heappop
from collections import deque
def solution(jobs):
    jobs.sort()
    len_jobs = len(jobs)
    jobs = deque([[x[1], x[0]] for x in jobs])
    jobq = []
    heappush(jobq, jobs.popleft())
    waitt = 0
    curt = 0
    while jobq:
        dur, rqt = heappop(jobq)
        curt = max(rqt, curt) + dur
        waitt += (curt - rqt)
        while jobs and jobs[0][1] <= curt:
            heappush(jobq, jobs.popleft())
        if jobs and len(jobq) == 0:
            heappush(jobq, jobs.popleft())
            
    return waitt//len_jobs




















#import heapq
#from collections import deque
#
#def solution(jobs):
#    jobs.sort()
#    
#    tasks = deque([[x[1], x[0]] for x in jobs])
#    
#    cur_t, wait_t = 0,0
#    rhq = []
#    heapq.heappush(rhq, tasks.popleft())
#    while rhq:
#        duration, req_t = heapq.heappop(rhq)
#        cur_t = max(cur_t, req_t) + duration
#        
#        #현재 task duration
#        wait_t += (cur_t - req_t)
#        
#        while tasks and tasks[0][1] <= cur_t:
#            heapq.heappush(rhq, tasks.popleft())
#        
#        if tasks and len(rhq)==0:
#            heapq.heappush(rhq, tasks.popleft())
#    
#    return wait_t // len(jobs)
        
















#import heapq
#from collections import deque
#
## 총 걸리는 시간은 상관없고, 각 프로세스 요청부터 종료까지 걸리는 시간의 평균이 최소가 되면 됨
#def solution(jobs):
#    # heapq 를 소요시간 기준으로 쓰기 위해 소요시간을 앞으로 가져오며
#    # sort는 x[1] x[0] 을 뒤집고 또 뒤집었으므로, 요청시점이 작은 순서대로 정렬
#    # tasks 는 수행할 작업의 리스트를 의미함
#    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
#    #print(f"jobs {jobs}, tasks {tasks}")
#    q = []
#    # q 는 tasks 중 실행을 요청한 작업을 의미함
#    heapq.heappush(q, tasks.popleft())
#    current_time, total_response_time = 0, 0
#    while len(q) > 0:
#        # print(heapq) 가 실패한 이유는 무엇입니까? 
#        
#        # A: heapq 는 객체가 아니고 모듈이니까
#        #print(f"heapq {q}")
#        dur, arr = heapq.heappop(q)
#        #print(f"dur {dur} arr {arr} max1<ct+dur> {current_time+dur} max2<arr+dur> {arr+dur}")
#        # max 는 왜 필요합니까? 
#        
#        # A: 마지막으로 task 가 종료된 시점과 다음 task의 요청시점 중 더 큰 값부터 소요시간을 계산해야 하기 때문
#        # 다음 task 의 요청시점이 엄청 커도 상관없음. 중요한 건 요청 이후 종료까지의 최소값을 찾는 것임.
#        current_time = max(current_time + dur, arr + dur)
#        total_response_time += current_time - arr
#        #print(f"ct {current_time} trt {total_response_time}")
#        # 아래 while 문 if 문 없이 그냥 한번에 heapq 에 넣고 돌리면 왜 일부 테스트 케이스는 실패합니까?
#        
#        # A1: 모든 task 에 대해 무작정 소요시간 작은 것부터 하면 안됨.
#        # 예) [요청, 소요] 일때, [[1000,1],[1,100]] 에 대해 
#        #     - [0] 먼저 실행하면, [1] 은 999ms 기다려야 함.
#        #     - [1] 먼저 실행하면, [0] 은 0ms 로 기다림 없음(1000ms 에 요청하니까).
#        # A2: current_time에 이미 요청된 것들은 무조건 소요시간 작은 것부터 하면 됨.
#        # 예) [[1000,1],[1,100],[0,10000]] 에 대해 [2] 실행 후, [0][1] 은 이미 요청된 상황일 때,
#        #     - [1] 을 먼저 실행하면, [0][1] 두 개가 100ms 를 기다린 후, [0] 한 개가 1ms 기다림. 총 201ms.
#        #     - [0] 을 먼저 실행하면, [0][1] 두 개가 1ms 를 기다린 후, [1] 한 개가 100ms 기다림. 총 102ms.
#        
#        # while 은 왜 필요합니까?
#        
#        # A: tasks 는 이미 요청시점으로 오름차순 정렬되어 있으므로, 요청시점이 가장 작은 [0] task 의 요청시점 [1] <= current_time 인 task 는 일단 모두 heapq 에 넣음
#        while len(tasks) > 0 and tasks[0][1] <= current_time:
#            heapq.heappush(q, tasks.popleft())
#        
#        # if 는 왜 필요합니까?
#        
#        # while 했는데 q에 아무것도 없으면 그냥 조건 상관없이 task를 q 에 넣음
#        if len(tasks) > 0 and len(q) == 0:
#            heapq.heappush(q, tasks.popleft())
#            
#    return total_response_time // len(jobs)

# 2402
#from heapq import heappush, heappop, heapify
#from collections import deque
#
#def solution(jobs):
#    rhq = []
#    jobs = deque(sorted([[job[1], job[0]] for job in jobs], key=lambda x: x[1]))
#    cur_t = 0
#    wait_t = 0
#    len_ = len(jobs)
#    heappush(rhq, jobs.popleft())
#    while rhq:
#        dur, rq_t = heappop(rhq)
#        cur_t = max(cur_t+dur, rq_t+dur)
#        print(cur_t)
#        wait_t += cur_t-rq_t
#        while jobs and jobs[0][1] < cur_t:
#            heappush(rhq, jobs.popleft())
#        if jobs and len(rhq) == 0:
#            heappush(rhq, jobs.popleft())
#    
#    return wait_t // len_



# 240319 틀림
#from heapq import heapify, heappush, heappop
#def solution(jobs):
#    jobs = list(map(lambda x:[x[1]+x[0], x[1], x[0]], jobs))
#    jobs = sorted(jobs, key=lambda x:x[0])
#    print(jobs)
#    # 경우의 수
#    # - 끝나는 시간 순서대로 먼저 처리
#    # - 끝나는 시간이 같으면 시작시간이 빠른 순으로 먼저 처리
#    # ex) 	[[8, 5, 3], [15, 8, 7], [15, 6, 9]] 일 때, [[끝나는 시각(시작 + 걸리는), 걸리는 시간, 시작 시각], ... ]
#    # 1. [8, 5, 3]  > 3 부터 8 까지 = 5
#    # 2. [15, 8, 7] > 7 들어와서, 8 부터 16 까지 = 9
#    # 3. [15, 6, 9] > 9 들어와서, 16 부터 22 까지 = 13
#    # 총 27
#    
#    # - 끝나는 시간 순서대로 먼저 처리
#    # - 끝나는 시간이 같으면 걸리는 시간이 적은 순으로 먼저 처리
#    # ex) 	[[8, 5, 3], [15, 8, 7], [15, 6, 9]] 일 때, [[끝나는 시각(시작 + 걸리는), 걸리는 시간, 시작 시각], ... ]
#    # 1. [8, 5, 3]  > 3 부터 8 까지 = 5
#    # 2. [15, 6, 9] > 9 들어와서, 9 부터 15 까지 = 6
#    # 3. [15, 8, 7] > 7 들어와서, 15 부터 23 까지 = 16
#    # 총 27
#    
#    answer = 0
#    cur_t = 0
#    for job in jobs:
#        done, elt, reqt = job
#        if cur_t == 0:
#            answer += elt
#            cur_t = elt+reqt
#        else:
#            answer += elt + (cur_t - reqt)
#            cur_t = cur_t+elt
#        #print(cur_t, answer)
#    
#    return answer/len(jobs)

# 240320
#from heapq import heappush, heappop
#from collections import deque
#def solution(jobs):
#    len_jobs = len(jobs)
#    jobs = deque(sorted([[x[1], x[0]] for x in jobs], key=lambda x:(x[1], x[0]))) # NOTE 틀린 부분. 여기서 key 를 x[1] --> (x[1], x[0]) 바꿨더니 통과함. 즉, 요청시간 x[1] 뿐만아니라, duration x[0] 도 같이 sort 를 해줘야 모두 통과한다는 뜻.
#    q, cur_t, answer = [], 0, 0
#    heappush(q, jobs.popleft())
#    while q:
#        dur, st = heappop(q)
#        cur_t = max(cur_t, st) + dur
#        answer += (cur_t-st)
#        while jobs and jobs[0][1] <= cur_t: # NOTE 틀린 부분. 어차피 정렬되어 있으니, 그냥 popleft 하면 됨.
#            heappush(q, jobs.popleft())
#        if jobs and len(q) == 0: # NODE 틀린 부분. jobs 는 비면 안되고, q 는 비어야 함.
#            heappush(q, jobs.popleft())
#        #print(cur_t, answer, q)
#    
#    return answer//len_jobs # NOTE 틀린 부분. "소수점 이하의 수는 버립니다."


