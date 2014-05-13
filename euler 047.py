def make_primes(to):
    result = []
    n = 2
    while len(result) < to:
        for i in range(2, int(n**0.5 + 1)):
            if n%i == 0: break
        else:
            result.append(n)
        n += 1
    return result
    
primes = make_primes(20000)

def factorization(num):
    divisors = []
    left = num
    while left != 1:
        for prime in primes:
            if left % prime == 0:
                left = left // prime
                divisors.append(prime)
                break
    return divisors

def product(L):
    from functools import reduce
    return reduce(lambda a,b:a*b, L)

# testing
# print (factorization(644), factorization(645), factorization(646), factorization(14), factorization(15), factorization(13), sep = "\n")

i = 210
flag = [False]
while not all(flag):
    n1, n2, n3, n4 = factorization(i), factorization(i+1), factorization(i+2), factorization(i+3)
    flag = map(lambda x: len(set(x)) >= 4, (n1, n2, n3, n4))
    i += 1

print ("%d = %s\n%d = %s\n%d = %s\n%d = %s" % (product(n1), n1, product(n2), n2, product(n3), n3, product(n4), n4))


