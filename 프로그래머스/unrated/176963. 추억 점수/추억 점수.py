def solution(name, yearning, photo):
    answer = []
    dict = {}
    for i in range(len(name)):
        dict[name[i]] = yearning[i]

    for i in range(len(photo)):
        for j in range(len(photo[i])):
            if photo[i][j] in dict.keys():
                photo[i][j] = dict[photo[i][j]]
            else:
                photo[i][j] = 0
    for i in photo:
        answer.append(sum(i))
    
    return answer