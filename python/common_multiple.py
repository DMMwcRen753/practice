#最小公倍数
import math
a = int(input())
b = int(input())

math.gcd(a, b)

lcm = a*b/math.gcd(a,b)

print(lcm)