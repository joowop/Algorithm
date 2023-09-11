def bin(n):
    a = []
    while True:
        if n % 2 == 0:
            n = n // 2

        elif n % 2 == 1:
            n = n // 2
            a.append(1)
        if n == 0:
            break
    return len(a)
               
def solution(n):
    answer = 0
    num1 = bin(n)
    while True:
        n += 1
        num = bin(n)
        if num1 == num:
            answer = n
            break
    return answer