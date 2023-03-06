import itertools
def solution(number):
    answer = 0
    coms = itertools.combinations(number, 3)
    for com in coms:
        if sum(com) == 0:
            answer+=1
        else:
            continue
    return answer