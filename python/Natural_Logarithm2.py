#3 定義に従って自然対数を計算
for h in range(1,10001):
    e=(1+1/h)**h
    if h%1000==0:
        print('h=',h,':',e)