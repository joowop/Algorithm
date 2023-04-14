T = int(input())
for i in range(1, T+1):
    num = list(map(int, input().split()))
    if num[0] > num[1]:
        print("#"+str(i),">")
    elif num[0] < num[1]:
        print("#"+str(i),"<")
    elif num[0] == num[1]:
        print("#"+str(i),"=")