T = int(input())

n = list(map(int, input().split()))
n.sort()
median = 0
idx = 0

idx = len(n)//2+1
median=n[idx-1]
print(median)