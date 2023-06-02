T = input().upper()
word = list(set(T))
result = []
for i in word:
    cnt = T.count(i)
    result.append(cnt)
if result.count(max(result)) > 1:
    print('?')
else:
    max_idx = result.index(max(result))
    print(word[max_idx])