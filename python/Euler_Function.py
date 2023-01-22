import math

num = int(input())

def phi(num):
    cnt=0
    for i in range (1,num+1):
        if math.gcd(num,i)==1:
            cnt+=1
    return cnt
    
print(phi(num))