def solution(num):
    answer = 0
    i = 0
    while (i<=500):
        i+=1
        if num == 1:
            answer = 0
            break
        elif num % 2 == 0:
            num = num/2
        elif num % 2 == 1:
            num = (num*3)+1
        answer += 1
        if i == 500:
            answer = -1
            break
        if num == 1:
            break
    return answer