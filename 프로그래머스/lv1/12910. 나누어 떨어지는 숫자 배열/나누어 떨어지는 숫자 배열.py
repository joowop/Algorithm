def solution(arr, divisor):
    a = []
    for i in range(len(arr)):
        if arr[i]%divisor == 0:
            a.append(arr[i])
    if len(a) == 0:
        a = [-1]
    return sorted(a)