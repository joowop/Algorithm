def solution(brown, yellow):
    area = brown + yellow # 넓이
    for i in range(3, (area//2) + 1):
        if area % i == 0: # 후보 찾는 중
            if 2*(area//i + i) - 4 == brown:
            # 2 * (가로 후보 + 세로 후보) - 4 == 둘레
                return [area//i, i]