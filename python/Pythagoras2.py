#ピタゴラスの定理で整数の組み合わせを求める

count = 0

for c in range(1,100):
    for b in range(1,c):
        for a in range(1,b):
            if a*a+b*b == c*c:
                check = 1
                for i in range(2,a):
                    if a%i == 0 and b%i == 0 and c%i == 0:
                        check = 0
                if check == 1:
                    count += 1
                    print(count," ",a,b,c)
print('fin')