ans = [1,1,2,2,2,8]

T = list(map(int, input().split()))
result = []
for idx, i in enumerate(T):
    cnt = 0
    if i == ans[idx]:
        cnt = 0
        result.append(str(cnt))
    else:
        cnt = ans[idx] - i
        result.append(str(cnt))
print(' '.join(result))
   