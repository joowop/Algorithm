n, m = map(int, input().split())
n = [nn+1 for nn in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    l = n[i-1:j][::-1]
    n[i-1:j] = l
for k in n:
    print(k, end=' ')