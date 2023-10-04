import math
def lcm(a, b):
    return a*b // math.gcd(a, b)

def solution(arr):
    n = arr[0]
    print(n,"nn")
    for i in arr[1:]:
        n = lcm(n, i)
        print(n)
    return n