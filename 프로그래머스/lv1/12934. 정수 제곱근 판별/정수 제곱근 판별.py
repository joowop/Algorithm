def solution(n):
    import math
    answer = 0
    if math.sqrt(n)% 2 == 0 or math.sqrt(n)% 2 == 1:
        n = int(math.sqrt(n))+ 1
        answer = n*n
    else :
        answer = -1
    return answer