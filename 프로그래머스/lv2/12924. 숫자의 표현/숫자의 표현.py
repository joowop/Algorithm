def solution(n):
    answer = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            # print(i, j)
            sum += j
            # print(j, sum)
            if sum == n:
                answer += 1
            elif sum > n:
                break
            
    return answer