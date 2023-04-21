a = int(input())
for i in range(1, a+1):
    b = int(input())
    
    c = list(map(int, input().split()))
    max_c = c[-1]
    max_profit = 0
    for idx in range(len(c)-1, -1, -1):

        if c[idx]<max_c:

            max_profit += max_c-c[idx]
        elif c[idx] > max_c:

            max_c = c[idx]
    print(f"#{i} {max_profit}")