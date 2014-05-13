import myprofiler

def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

sumPrimes = 0
i = 2

with myprofiler.profile():
    
    while i < 2000000:
        if is_prime(i):
            sumPrimes += i
        i += 1

print("Sum of all the primes below two million: %d" % sumPrimes)
