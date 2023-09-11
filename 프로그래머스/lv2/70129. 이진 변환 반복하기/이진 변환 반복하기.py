def solution(s):
    answer = []
    b = []
    num = 0
    while True:
        num += 1
        for i in s:
            if i == '1':
                answer.append(i)
            elif i == '0':
                b.append(i)
        s = bin(len(answer))
        answer = []
        s = s[2:]
        if s == '1':
            break
    return [num, len(b)]