def solution(enroll, referral, seller, amount):
    answer = []
    return answer

def solution(enroll, referral, seller, amount) :
    # enroll은 노드, referral은 부모
    # seller와 amount를 순회하며 이익 계산
    # 현재 직원의 이익 계산 -> 부모의 이익 계산 : 루트까지 while문으로 돌리기

    node_dict = dict(zip(enroll, referral))     # 직원별 추천인 연결 딕셔너리 - { 직원 명 : 추천 직원 명}

    total = {name : 0 for name in enroll}       # 직원별 수익 딕셔너리 - { 직원 명 : 수익 } - 초기값은 0

    for man, amt in zip(seller, amount):    # 판매직원과 판매량을 순회
        p = amt * 100   # 판매수익

        curr = man  # 실 판매직원부터 시작

        while curr != "-" and p > 0 :   # 루트 노드가 아니고, 계산할 수익이 0보다 큼
            total[curr] += p - p // 10  # 수익의 10퍼센트를 제외하고 현재 직원의 수익에 더함
            curr = node_dict[curr]      # 다음 계산할 직원은 현재 직원의 추천인
            p //= 10    # 추천인의 수익은 현재 직원의 10퍼센트

    return [total[i] for i in enroll]