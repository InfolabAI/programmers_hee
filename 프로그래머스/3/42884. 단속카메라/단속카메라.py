#def solution(routes):
#    return 0
# 240229
def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x:x[1]) # NOTE 틀렸던 부분. 결국 맞춤. x[0] 이 아니라 x[1] 로 sort 해야함. x[0] 으로만 sort 하면 route[i] 이 route[i+1] 을 아예 포함할 수가 있음.
    carmera = -30001
    #print(routes)
    
    for car in routes:
        st, ed = car
        if st > carmera:
            answer += 1
            carmera = ed
        #print(st, ed, carmera, answer)
        
    return answer













# https://somjang.tistory.com/entry/Programmers-%ED%83%90%EC%9A%95%EB%B2%95Greedy-%EB%8B%A8%EC%86%8D%EC%B9%B4%EB%A9%94%EB%9D%BC-Python
#def solution(routes):
#    answer = 0
#    camera_position = -30001
#    routes.sort(key=lambda x: x[1])
#    print(routes)
#    
#    for route in routes:
#        if camera_position < route[0]:
#            answer += 1
#            camera_position = route[1]
#    
#    return answer

# 240123 버전
#def solution(routes):
#    answer = 0
#    cp = -30001
#    routes = sorted(routes, key=lambda x:x[1])
#    #print(routes)
#    
#    for r in routes:
#        if cp < r[0]:
#            answer += 1
#            cp = r[1]
#    
#    return answer

# 240124 버전
#def solution(routes):
#    answer = 0
#    routes = sorted(routes, key=lambda x:x[1])
#    cp = -30001
#    for r in routes:
#        if cp < r[0]:
#            answer += 1
#            cp = r[1]
#    
#    return answer

