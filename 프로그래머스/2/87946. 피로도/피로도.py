import itertools
def solution(k, dungeons):
    answer = []
    k2 = k
    n = list(itertools.permutations(dungeons, len(dungeons)))
    for i in n:
        # print(i)
        cnt = 0
        k = k2
        for j in i:
            
            # print("k:::::::::::",k)
            # print(j)
            if j[0] <= k:
                k = k -j[1]
                cnt += 1
                
                
            else:
                continue
        answer.append(cnt)
    # print("answer",answer)
    return max(answer)