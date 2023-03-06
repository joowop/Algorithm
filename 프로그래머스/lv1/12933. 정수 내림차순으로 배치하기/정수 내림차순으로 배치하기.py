def solution(n):
    answer = []
    for i in str(n):
        answer.append(i)
    answer.sort()
    answer.reverse()
    answer = ''.join(answer)
    return int(answer)