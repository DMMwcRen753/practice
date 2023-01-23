# 1 虚数単位の計算
im = 1j
print(im)
print(type(im))
print(im**2)
print(type(im))

#2 複素数の表現
cn = 2 + 3j
print(cn)
cf=complex(2,3)
print(cf)
print(cn==cf)

#3 複素数に関する関数
print(cf.real)
print(cf.imag)
print(cf.conjugate())

#4 cmath関数を使った負の実数の平方根の計算
import cmath
z1 = cmath.sqrt(-1)
print(z1)
print(type(z1))
z2 = cmath.sqrt(-1)+2
print(z2)