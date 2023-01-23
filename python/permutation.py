#1 定義通りの方法で順列の計算をする

n,r = int(input()),int(input())

def nPr(n,r):
    npr=1
    for i in range(n,n-r,-1):
        npr*=i
    return npr
print(nPr(n,r))

def nCr(n,r):
    factr =1
    r = min(r, n-r)
    for i in range(r,1,-1):
        factr*=i
    return nPr(n,r)/factr    
print(nCr(n,r))