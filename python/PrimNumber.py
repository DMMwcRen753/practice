#素数の数をすべて求める

limit = int(input())

def prime(limit):
    prime = []
    for i in range(2,limit):
        for j in range(2, int(limit**0.5)+1):
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime
print(prime(limit))