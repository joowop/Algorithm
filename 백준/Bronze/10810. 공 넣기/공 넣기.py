#  바구니 개수, max 공 번호
a, b = map(int, input().split())
a = [0 for i in range(int(a))]
for l in range(b):
    l = list(map(int, input().split()))
    if l[0] == l[1]:
        a[l[0]-1] = l[2] 
    else:
        a[l[0]-1:l[1]] = [l[2] for j in a[l[0]-1:l[1]]]

for k in a:
    print(k, end=' ')