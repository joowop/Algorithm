n = [i+1 for i in range(30)]

for j in range(len(n)-2):
    m = input()
    if int(m) in n:
        n.remove(int(m))
    else :
        continue

for k in n:
    print(k)