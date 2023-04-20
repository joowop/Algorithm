T = list(map(int, input().split()))
if T[0] == 1 and T[1] == 2:
    print("B")
elif T[0] == 1 and T[1] == 3:
    print("A")
elif T[0] == 2 and T[1] == 1:
    print("A")
elif T[0] == 2 and T[1] == 3:
    print("B")
elif T[0] == 3 and T[1] == 1:
    print("B")
elif T[0] == 3 and T[1] == 2:
    print("A")