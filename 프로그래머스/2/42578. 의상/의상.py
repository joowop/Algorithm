import itertools
def solution(clothes):
    answer = 1
    dic = {}
    for v, k in clothes:
        if k in dic:
            dic[k].append(v)
        else:
            dic[k] = [v]
    print(dic)
    # n = itertools.permutations(dic)
    for value in dic.values():
        answer *= len(value) + 1
        # print(value)
    return answer-1