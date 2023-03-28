def solution(array, commands):
    answer = []
    for i in commands:
        # answer.append(array[i[0]-1:i[1]])
        answer.append(sorted(array[i[0]-1:i[1]])[i[2]-1:i[2]])
    a = []
    for i in answer:
        for j in i:
            a.append(j)
        
    return a