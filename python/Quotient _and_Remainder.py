#商と余りの計算

xp = int(input())
y = int(input())

xm = xp*(-1)

print('divmod({},{})------'.format(xp,y))
print(divmod(xp, y))
quotient, remainder = divmod(xp, y)
print('商：', quotient)
print('余り：', remainder)
print('divmod({},{})------'.format(xm,y))
print(divmod(xm, y))
quotient, remainder = divmod(xm, y)
print('商：', quotient)
print('余り：', remainder)