def solution(a, b):
    answer = 0
    if a< b or a == b :
        answer = sum([i for i in range(a,b+1)])
    elif a > b :
        answer = sum([i for i in range(b, a+1)])
    return answer