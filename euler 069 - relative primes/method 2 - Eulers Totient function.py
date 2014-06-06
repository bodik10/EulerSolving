primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# 30 -> [2, 3, 5] - all prime divisors
def p_n(n):
    result = []
    i = 0
    while primes[i] <= n/2:
        if n % primes[i] == 0: result.append(primes[i])
        i += 1
    return result

from functools import reduce

# look at figure
def phi(n):
    if n in primes:
        return n-1
    
    return int( reduce(lambda a, p: a*(1-1/p), p_n(n), n) ) # ! USAGE OF REDUCE
                                                            # in product operations (look at figure)

# testing
if __name__ == "__main__":
    for n in range(2, 21):
        print ("φ(%d) = %d" % (n, phi(n)))

# solving problem by this method is inpossible - to slow
