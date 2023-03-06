def solution(n):
    answer = 0
    a = []
    for i in range(n):
        if n%(i+1) == 0:
            a.append(i+1)
        else:
            continue
    answer = sum(a)
    return answer