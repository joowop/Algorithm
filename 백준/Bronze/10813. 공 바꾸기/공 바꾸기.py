n, m = map(int, input().split())
# [1,2,3,4,5]
n = [bk+1 for bk in range(n)]
for i in range(m):
    # M번 만큼 공을 바꿈
    i,j = list(map(int, input().split()))
    n[i-1], n[j-1] = n[j-1], n[i-1]
    
for aa in n:
    print(aa, end=' ')