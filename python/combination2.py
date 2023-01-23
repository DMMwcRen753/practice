#3 組合せの定理から再帰関数により組合せを計算する

n,r = int(input()),int(input())

def comb_r(n, r):
    if r==0:
        return 1
    return comb_r(n-1, r-1) * n / r
print(comb_r(n,r))