def solution(order):
    cnt = 0
    con = [x for x in range(len(order), 0, -1)]
    extra = []
    while True:
        if con:
            extra.append(con.pop())
            
            while extra and extra[-1] == order[cnt]:
                extra.pop()
                cnt+=1
        else:
            break
    # print(con)
    return cnt