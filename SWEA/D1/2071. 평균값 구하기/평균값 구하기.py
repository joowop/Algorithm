T = int(input())
answer = 0
for i in range(1,T+1):
    num = list(map(int, input().split()))
    answer = sum(num)/10
    print("#"+str(i),round(answer))
    