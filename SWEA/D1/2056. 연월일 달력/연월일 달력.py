T = int(input())
month = [31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(1, T+1):
    num = str(input())
    m = list(num)
    if int(''.join(m[4:6])) == 1 and int(''.join(m[6:8])) >=1 and int(''.join(m[6:8])) <= 31:
        print("#"+str(i),''.join(m[0:4])+"/"+''.join(m[4:6])+"/"+''.join(m[6:8]))
    elif int(''.join(m[4:6])) == 2 and int(''.join(m[6:8])) >=1 and int(''.join(m[6:8])) <= 28:
        
        print("#"+str(i),''.join(m[0:4])+"/"+''.join(m[4:6])+"/"+''.join(m[6:8]))
    elif int(''.join(m[4:6])) == 3 and int(''.join(m[6:8])) >=1 and int(''.join(m[6:8])) <= 31:
        print("#"+str(i),''.join(m[0:4])+"/"+''.join(m[4:6])+"/"+''.join(m[6:8]))
    elif int(''.join(m[4:6])) == 4 and int(''.join(m[6:8])) >=1 and int(''.join(m[6:8])) <= 30:
        print("#"+str(i),''.join(m[0:4])+"/"+''.join(m[4:6])+"/"+''.join(m[6:8]))
    elif int(''.join(m[4:6])) == 5 and int(''.join(m[6:8])) >=1 and int(''.join(m[6:8])) <= 31:
        print("#"+str(i),''.join(m[0:4])+"/"+''.join(m[4:6])+"/"+''.join(m[6:8]))
    elif int(''.join(m[4:6])) == 6 and int(''.join(m[6:8])) >=1 and int(''.join(m[6:8])) <= 30:
        print("#"+str(i),''.join(m[0:4])+"/"+''.join(m[4:6])+"/"+''.join(m[6:8]))
    elif int(''.join(m[4:6])) == 7 and int(''.join(m[6:8])) >=1 and int(''.join(m[6:8])) <= 31:
        print("#"+str(i),''.join(m[0:4])+"/"+''.join(m[4:6])+"/"+''.join(m[6:8]))
    elif int(''.join(m[4:6])) == 8 and int(''.join(m[6:8])) >=1 and int(''.join(m[6:8])) <= 31:
        print("#"+str(i),''.join(m[0:4])+"/"+''.join(m[4:6])+"/"+''.join(m[6:8]))
    elif int(''.join(m[4:6])) == 9 and int(''.join(m[6:8])) >=1 and int(''.join(m[6:8])) <= 30:
        print("#"+str(i),''.join(m[0:4])+"/"+''.join(m[4:6])+"/"+''.join(m[6:8]))
    elif int(''.join(m[4:6])) == 10 and int(''.join(m[6:8])) >=1 and int(''.join(m[6:8])) <= 31:
        print("#"+str(i),''.join(m[0:4])+"/"+''.join(m[4:6])+"/"+''.join(m[6:8]))
    elif int(''.join(m[4:6])) == 11 and int(''.join(m[6:8])) >=1 and int(''.join(m[6:8])) <= 30:
        print("#"+str(i),''.join(m[0:4])+"/"+''.join(m[4:6])+"/"+''.join(m[6:8]))
    elif int(''.join(m[4:6])) == 12 and int(''.join(m[6:8])) >=1 and int(''.join(m[6:8])) <= 31:
        print("#"+str(i),''.join(m[0:4])+"/"+''.join(m[4:6])+"/"+''.join(m[6:8]))

    else:
        print("#"+str(i),-1)
