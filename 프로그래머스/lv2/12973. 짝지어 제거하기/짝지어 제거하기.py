def solution(s):
    answer = 0
    tmp = []
    for i in s:
        tmp.append(i)
        
        if len(tmp) > 1 and tmp[-1] == tmp[-2]:
            tmp.pop()
            tmp.pop()
        
        if len(tmp) == 0:
            answer = 1
        else:
            answer = 0
    return answer