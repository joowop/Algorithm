def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i, num in enumerate(numbers):
        
        while stack and num > numbers[stack[-1]]:
            
            j = stack.pop()
            answer[j] = num
        stack.append(i)

    return answer