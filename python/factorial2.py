def factorial2_while(num):
    val = 1
    while num > 0:
        val *= num
        num -= 2
    return val
print(10, 'even', 10*8*6*4*2, factorial2_while(10))
print(11, 'odd ', 11*9*7*5*3*1, factorial2_while(11))