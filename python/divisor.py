#約数を全て求めリスト化
num = int(input())
def divisors_list_s(num):
    divisors = []
    for i in range(1,int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)
            if i*i == num:
                continue
            divisors.append(int(num/i))
    return sorted(divisors)
print(divisors_list_s(num))