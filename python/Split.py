#4 組合せの分割の定理から再帰関数により組合せを計算する
def comb(n,r):
    if r == 0:
        return 1
    elif n < r:
        return 0
    else:
        return comb(n-1, r) + comb(n-1, r-1)
    
print(comb(5,3))