def solution(s):
    answer = ''
    a = [i for i in s]
    if (len(a)%2) == 0:
        answer = ''.join(a[int(len(a)/2)-1:int(len(a)/2)+1])
    elif (len(a)%2) == 1:
        answer = a[int(len(a)/2)]
    return answer