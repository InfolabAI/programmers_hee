def solution(n, t, m, timetable):
    return

# 240809
import datetime
def solution(n, t, m, timetable):
    timetable_m = []
    # 문자열 > 분
    for tt in timetable:
        timetable_m.append(int(tt[:2])*60 + int(tt[3:5]))
    timetable_m = sorted(timetable_m)
    last = timetable_m[-1]
    bustable_m = {9*60 + t*i:[] for i in range(n)}
    #print(timetable_m)
    for bt, bl in bustable_m.items():
        for i, tt in enumerate(timetable_m):
            if bt >= tt and len(bl) < m:
                bl.append(tt)
            else:
                timetable_m = timetable_m[i:]
                break
    # NOTE 틀린부분. 모든 버스 볼 필요없이, 마지막 버스에 탑승 가능한지 여부만 보면 됨. NOTE 또 틀린 부분. 마지막 버스가 차있어도 모두 타지 않았을 수 있음. 예를 들어, 테케7번은 마지막 버스가 다 찼고, 1명이 못탐. 그러므로, 대기열이 아닌 마지막 버스에 탄 사람보다 1분 일찍 와야 함
    #print(bustable_m)
    for bt, bl in reversed(bustable_m.items()):
        if len(bl) < m:
            ret = bt
        else:
            ret = bl[-1] - 1 # 여기가 last 가 아니라, bl[-1] 이어야 함
        break
    
    return str(ret//60).zfill(2) + ":" + str(ret%60).zfill(2) # NOTE 틀린부분. 양식 맞출땐 zfill 사용

#ref
#def solution(n, t, m, timetable):
#    answer = ''
#    # 문자열 시간을 분으로 변경
#    time = []
#    for times in timetable:
#        time.append(list(map(int, times.split(':'))))
#    # 오름차순 정렬
#    time = sorted([a*60+b for a, b in time])
#    # key:버스 출발 시각 dictionary생성
#    dic = {}
#    start = 540
#    for i in range(n):
#        dic[start+i*t] = []
#    # 오름차순으로 정렬된 크루들이 탑승 가능한 배차에 차례대로 배치
#    for i in time:
#        for k, v in dic.items():
#            # 정해진 m명 이하이고 해당 값이 출발시간보다 작을때 해당 배차에 추가
#            if len(v) < m and i <= k:
#                dic[k].append(i)
#                break
#    # 마지막 출발하는 버스 key값 확인
#    k = sorted(dic.keys(), reverse=True)
#    # 만약 해당 출발버스에 사람이 다 안차있다면 버스 출발시간 return
#    if len(dic[k[0]]) < m:
#        return str(k[0]//60).zfill(2) + ":" + str(k[0]%60).zfill(2)
#    # 해당 출발버스에 사람이 다 차있다면 마지막 사람보다 1분빨리오게 return
#    else:
#        temp = dic[k[0]][-1]-1
#        return str(temp//60).zfill(2) + ":" + str(temp%60).zfill(2)
#    return answer