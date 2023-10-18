import itertools
def an(n):
    a = []
    
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            a.append(i)
            if ( (i**2) != n):
                a.append(n//i)
    a.sort
    return a

def solution(numbers):
    
    answer = []
    
    for i in range(1, len(numbers)+1):
        n = list(itertools.permutations(numbers, i))
                 
        n = list(set(n))
        
        for j in n :
            
            a = int(''.join(list(j)))

            if len(an(a)) == 2:
                
                answer.append(a)
                answer = list(set(answer))
            
    return len(answer)