#2 decimalモジュールによる自然対数を
import decimal 
decimal.getcontext().prec = 30
print(decimal.Decimal(1).exp())
print(decimal.Decimal(3).exp())