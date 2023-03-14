def solution(s):
    a = s.split(" ")

    c = []
    for i in range(len(a)):
        b = []
        for j,k in zip(range(len(a[i])), a[i]):
            if j%2 == 0:
                b.append(k.upper())
            elif j%2 == 1:
                b.append(k.lower())
        c.append(''.join(b))
    return " ".join(map(str, c))