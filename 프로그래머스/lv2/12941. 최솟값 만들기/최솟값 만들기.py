def solution(A,B):
    answer = 0
    for i, j in zip(list(sorted(A)), list(reversed(sorted(B)))):
        answer += (i*j)
    # print(list(reversed(B)))
    # a = 0
    # for _ in range(len(A)):
    #     a = min(A) * max(B)
    #     A.remove(min(A))
    #     B.remove(max(B))
    #     answer += a
    
    return answer