def solution(numbers):
    numbers_str = [str(num) for num in numbers]
    
    numbers_str.sort(key=lambda num: num*3, reverse=True)
    # print(numbers_str)
    return str(int(''.join(numbers_str)))