n = int(input())
num = []
for i in range(n+1):
    num.append(str(i))
a = ' '.join(reversed(num)).split()
for i in a:
    print(i,end=" ")