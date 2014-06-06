def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if not num % i:
            return False
    return True

primes = [i for i in range(2,100) if is_prime(i)]

from fractions import gcd

# 9 -> [1,2,4,5,7,8] - return all coprimes
def relatively_prime(n):
    if n in primes:
        return list(range(1, n))
    result = [1]
    for i in range(2, n):
        if gcd(n, i) == 1:
            result.append(i)
    return result

# 9 -> 6 - return number of coprimes
def phi(n):
    if n in primes:
        return n-1
    result = 1
    for i in range(2, n):
        if gcd(n, i) == 1:
            result += 1
    return result

# testing
if __name__ == "__main__":
    for n in range(2, 21):
        print ("φ(%d) = %d\t%s" % (n, phi(n), relatively_prime(n)))

# solving problem by this method is inpossible - to slow (~500 billion iter)
