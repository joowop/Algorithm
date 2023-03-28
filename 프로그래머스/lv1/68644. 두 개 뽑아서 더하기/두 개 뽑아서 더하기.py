import itertools
def solution(numbers):
    b = []
    a = list(itertools.combinations(numbers,2))
    for i in a:
        b.append(sum(i))
    c = set(b)
    answer = list(c)
    return sorted(answer)