def solution(a, b):
    answer = ''
    day = ['FRI','SAT', 'SUN','MON','TUE','WED','THU']
    count = 0
    cd = []
    for i in range(53):
        for idx, j in enumerate(day):
            cd.append(j)

    cd = cd[:366]
    dic = {}
    dic[1] = cd[:31]
    dic[2] = cd[31:60]
    dic[3] = cd[60:91]
    dic[4] = cd[91:121]
    dic[5] = cd[121:152]
    dic[6] = cd[152:182]
    dic[7] = cd[182:213]
    dic[8] = cd[213:244]
    dic[9] = cd[244:274]
    dic[10] = cd[274:305]
    dic[11] = cd[305:335]
    dic[12] = cd[335:366]

    for k, v in dic.items():
        if k == a:
            answer = v[b-1]
    return answer