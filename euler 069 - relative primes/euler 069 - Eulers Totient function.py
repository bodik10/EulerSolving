def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if not num % i:
            return False
    return True

primes = [i for i in range(2,1000001) if is_prime(i)]

def p_n(n):
    result = []
    i = 0
    while primes[i] <= n/2:
        if n % primes[i] == 0: result.append(primes[i])
        i += 1
    return result

from functools import reduce
def phi(n):
    if n in primes:
        return n-1
    return int( reduce(lambda a, p: a*(1-1/p), p_n(n), n) )


# solving problem
max, maxN = 0, 0

for n in range(2,11):
    φ = phi(n)
    if n/φ > max:
        max, maxN = n/φ, n

print ("n=%d for which n/φ(n)=%.5f is a maximum" % (maxN, max))
