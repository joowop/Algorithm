def solution(s):
    s= list(s)
    s.sort()
    a = []
    b = []
    for i in s:
        if i.isupper() == True:
             a.insert(0,i)
        else:
            b.insert(0,i)
    return ''.join(b + a)

