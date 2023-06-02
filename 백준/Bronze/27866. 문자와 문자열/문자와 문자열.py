S = str(input())

num = int(input())
for idx, i in enumerate(range(1, len(S)+1)):
    if i == num:
        print(S[idx])