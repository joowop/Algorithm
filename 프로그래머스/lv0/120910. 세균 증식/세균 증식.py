def solution(n, t):
    answer = 0
    for i in range(t+1):
        if i == 0:
            answer = n
        else :
            n = n * 2 
            answer = n
    return answer