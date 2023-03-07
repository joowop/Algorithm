def solution(n):
    answer = ''
    a = []
    for i in range(n):
        if i == 0 or i%2==0:
            a.append("수")
        elif i%1 == 0:
            a.append("박")
    answer = ''.join(a)
    return answer