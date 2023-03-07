def solution(phone_number):
    answer = ''
    a = []
    phone_number = list(phone_number)
    a = []
    for i in phone_number[:-4]:
        i = "*"
        a.append(i)
    answer = ''.join(a) +''.join(phone_number[-4:])   
    return answer