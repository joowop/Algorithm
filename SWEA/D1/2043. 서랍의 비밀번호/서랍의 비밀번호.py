a = list(map(int, input().split()))

P = a[0]
K = a[1]

answer = 0

while(True):
    K += 1
    answer += 1
    if K == P:
        break
print(answer+1)