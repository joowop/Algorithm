n = int(input())
m = 0
for i in range(1, n+1):
    num = list(map(int, input().split()))
    m = max(num)
    print("#"+str(i),m)