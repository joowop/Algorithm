def solution(s):
    words = s.split(" ")
    answer = []

    for i in words:
        if i !="":
            answer.append(i[0].upper() + i[1:].lower())
        else:
            answer.append("")
        
           
    return ' '.join(answer)