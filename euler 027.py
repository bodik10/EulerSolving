import math

def is_prime(num):
    if num < 1: return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if not num % i:
            return False
    return True

def f(a, b, n):
    return n**2 + a*n + b

def find_coefficients():
    maxN = maxA = maxB = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0
            while is_prime(f(a, b, n)):
                n += 1
            if n > maxN:
                maxN, maxA, maxB = n, a, b
            
    print("Coefficients %d and %d for the quadratic expression produces %d primes for consecutive values of n, starting with n = 0." % (maxA, maxB, maxN))
    print(maxA * maxB)

# testing results -61, 971
def test():
    for n in (0,1,2,3,5,10,26,50,70,-1,-2,-9,-50,-70):
        print("n=%d, f(n)=%d %s" % (n, f(-61, 971, n), "is prime!" if is_prime(f(-61, 971, n)) else""))
        
find_coefficients()
test()