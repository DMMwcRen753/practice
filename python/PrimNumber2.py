num = int(input())
flg = False
for i in range(2, int(num**0.5)+1):
    if num % i == 0:
        break
else:
    flg = True
print(flg)