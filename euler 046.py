class BreakException(Exception): pass

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
    
primes = make_primes(10000)

for num in (n for n in range(3, 10**6, 2) if n not in primes):
    try:
        for prime in primes:
            if prime + 2 > num: break
            i = Sum = 1
            while Sum < num:
                Sum = prime + 2*(i**2)
                i += 1
                assert not Sum == num
    except AssertionError:
        continue
    else:
        print ("%d is the smallest odd composite that cannot be written as the sum of a prime and twice a square" % num)
        break
        
