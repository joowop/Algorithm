import math

def solution(fees, records):
    # fish_data = [[a,b,c] for l,w in records.split(' ')]
    records_2d = [[j for j in record.split(' ')] for record in records]
    # print(records_2d)

    dic = {}
    for record_ in records_2d:
        if record_[1] in list(dic.keys()):
            dic[record_[1]].append(record_[0])
        else:
            dic[record_[1]] = [record_[0]]
    # print(dic)
    dic = dict(sorted(dic.items()))

    result = []
    for key, value in dic.items():
        if len(value)%2 == 1:
            value.append('23:59')
        # print(value)
        minute = 0
        for i in range(0, len(value), 2):
            in_ = value[i].split(':')
            out_ = value[i+1].split(':')
            min = (int(out_[0])-int(in_[0]))*60 + int(out_[1])-int(in_[1])
            minute += min
        print(minute)
        if (minute - fees[0]) < 0:
            pay = fees[1]
        else:
            pay = fees[1] + math.ceil((minute-fees[0])/fees[2]) * fees[3]
        print(pay)
        result.append(pay)

    return result