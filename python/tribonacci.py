a,b,c = 0,0,1
while a < 300:
    print(a,b,c,end=" ")
    a = b+c+a
    b = c+a+b
    c = a+b+c