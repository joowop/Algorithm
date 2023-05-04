import math

def solution(box, n):
    return math.prod(map(lambda v: v//n, box))