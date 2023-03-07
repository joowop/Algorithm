def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = absolutes[i]- (2*absolutes[i])
        else : 
            continue
        answer = sum(absolutes)
    return answer