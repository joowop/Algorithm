def solution(n):
    anwser = 0
    a = []
    for i in range(n):
        if i != 0 and n % i == 1:
            a.append(i)
        else :
            continue
    answer = min(a)
    return answer