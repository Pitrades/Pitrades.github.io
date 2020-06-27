import math


n = 600851475143
notFound = True
i = 1

def prim(x):
    if x==1:
        return False
    if x==2:
        return True
    for i in range(3, int(math.sqrt(x)+1), 2):
        if x%i==0:
            return False
    return True
while notFound:
    if prim(n/i) and int(n/i)==n/i:
        notFound = False
    i+=1



print(n/i)
