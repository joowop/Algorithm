T = int(input())
for i in range(1, T+1):
    a = list(map(int, input().split()))
    print("#"+str(i), a[0]//a[1], a[0]%a[1])