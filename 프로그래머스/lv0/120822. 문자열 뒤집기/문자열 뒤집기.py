def solution(my_string: str) -> str:
    return my_string[::-1]  # 역슬라이싱

if __name__ == '__main__':
    print(solution("jaron"))  # "noraj"
    print(solution("bread"))  # "daerb"