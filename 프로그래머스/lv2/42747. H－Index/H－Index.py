def solution(citations):
    citations.sort()  # 입력 리스트를 정렬합니다.
    n = len(citations)
    
    for i in range(n):
        if citations[i] >= n - i:
            return n - i  # H-Index를 찾았으므로 반환합니다.
    
    return 0  # H-Index를 찾지 못한 경우 0을 반환합니다.
