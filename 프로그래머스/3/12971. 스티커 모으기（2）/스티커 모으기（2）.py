def solution(sticker):
    answer = 0
    
    return answer


# ref(https://tiktaek.tistory.com/66)
def solution(sticker):
    if len(sticker) == 1: return sticker[0]
    answer = [[0 for i in range(len(sticker))] for j in range(2)]
    answer[0][0:2] = [sticker[0], sticker[0]]
    answer[1][1] = sticker[1]

    for idx in range(2, len(sticker)):
        answer[0][idx] = max(answer[0][idx-1], answer[0][idx-2]+sticker[idx])
        answer[1][idx] = max(answer[1][idx-1], answer[1][idx-2]+sticker[idx])

    return max(answer[0][-2], answer[1][-1])