def solution(t, p):
    answer = []
    count = 0
    for i in range((len(t)-len(p))+1):
        answer.append(t[0:len(p)])
        t = t[1:]
    for i in answer:
        if int(p) >= int(i):
            count +=1
    return count