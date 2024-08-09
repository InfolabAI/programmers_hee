def solution(n, t, m, timetable):
    answer = ''
    return answer
#ref
def solution(n, t, m, timetable):
    answer = ''
    # 문자열 시간을 분으로 변경
    time = []
    for times in timetable:
        time.append(list(map(int, times.split(':'))))
    # 오름차순 정렬
    time = sorted([a*60+b for a, b in time])
    # key:버스 출발 시각 dictionary생성
    dic = {}
    start = 540
    for i in range(n):
        dic[start+i*t] = []
    # 오름차순으로 정렬된 크루들이 탑승 가능한 배차에 차례대로 배치
    for i in time:
        for k, v in dic.items():
            # 정해진 m명 이하이고 해당 값이 출발시간보다 작을때 해당 배차에 추가
            if len(v) < m and i <= k:
                dic[k].append(i)
                break
    # 마지막 출발하는 버스 key값 확인
    k = sorted(dic.keys(), reverse=True)
    # 만약 해당 출발버스에 사람이 다 안차있다면 버스 출발시간 return
    if len(dic[k[0]]) < m:
        return str(k[0]//60).zfill(2) + ":" + str(k[0]%60).zfill(2)
    # 해당 출발버스에 사람이 다 차있다면 마지막 사람보다 1분빨리오게 return
    else:
        temp = dic[k[0]][-1]-1
        return str(temp//60).zfill(2) + ":" + str(temp%60).zfill(2)
    return answer