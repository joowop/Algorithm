import itertools
def solution(babbling):
    answer = 0
    a = ["aya", "ye", "woo", "ma"]
    aa = {}
    for s in babbling:
        if s in aa:
            aa[s] += 1
        else:
            aa[s] = 1

    count = 0

    for j in range(1,5):
        coms = itertools.permutations(a, j)

        for i in coms:
            if ''.join(i) in babbling and aa:
                answer += 1
    for k, j in aa.items():
        if j == 2:
            answer += 1
    return answer