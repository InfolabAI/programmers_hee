def solution(array, commands):
    answer = []
    for comm in commands:
        slice = sorted(array[comm[0]-1:comm[1]])
        answer.append(slice[comm[2]-1])
        
    return answer