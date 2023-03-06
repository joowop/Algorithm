def solution(s):
    answer = True
    a = []
    p = 0
    y = 0
    for i in s:
        a.append(i)
    p = a.count("p") + a.count("P")
    y = a.count("y") + a.count("Y")
    if p == y:
        answer = True
    else :
        answer = False
    return answer
