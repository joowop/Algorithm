ans = input()
cnt = len(ans) -1
result = []

for i in ans:
    if i == ans[cnt]:
        result.append(1)
    else:
        result.append(0)
    cnt -= 1
    
if 0 in result:
    print(0)
else:
    print(1)