def solution(numbers):
    all_nums = set(range(10))
    num_set = set(numbers)
    return sum(all_nums - num_set)
