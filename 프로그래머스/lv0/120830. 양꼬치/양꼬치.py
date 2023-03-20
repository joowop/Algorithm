def solution(n: int, k: int) -> int:
    return 12000 * n + 2000 * k - (n//10 * 2000)

if __name__ == '__main__':
    print(solution(10, 3))  
    print(solution(64, 6)) 