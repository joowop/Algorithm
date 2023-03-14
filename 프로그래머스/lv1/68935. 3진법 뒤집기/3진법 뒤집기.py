def solution(n):
    answer = 0
    arr = []
    while n >= 1:
        a = n%3
        arr.append(a)
        n = n//3
    arr.reverse()
    for i in range(len(arr)):
        answer += arr[i]*(3**i)
    return answer