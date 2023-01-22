num = int(input())

def prime_f_list(num):
    divisors = []
    for prime in range(2,num+1):
        while (num % prime) == 0:
            divisors.append(prime)
            num //= prime
    return divisors
    
print(prime_f_list(num))