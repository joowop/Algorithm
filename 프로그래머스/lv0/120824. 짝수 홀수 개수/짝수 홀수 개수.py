def solution(num_list):
    answer = []
    count = 0
    counts = 0
    for i in num_list:
        if i%2 == 0:
            count += 1
        
        else:
            counts += 1
    answer.append(count)
    answer.append(counts)
    return answer