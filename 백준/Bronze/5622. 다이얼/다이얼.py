al ='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
al = al.split()
result = []
call = str(input())

for i in call:
    if i in al[:3]:
        result.append(3)
    elif i in al[3:6]:
        result.append(4)
    elif i in al[6:9]:
        result.append(5)
    elif i in al[9:12]:
        result.append(6)
    elif i in al[12:15]:
        result.append(7)
    elif i in al[15:19]:
        result.append(8)
    elif i in al[19:22]:
        result.append(9)
    elif i in al[22:26]:
        result.append(10)
    
print(sum(result))
