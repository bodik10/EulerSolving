def isPrime(n):
    if n == 1: return False
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

def isTruncatable(num):
    s1 = str(num)[1:]
    s2 = str(num)[:-1]
    while s1:
        if not isPrime(int(s1)) or not isPrime(int(s2)):
            return False
        s1 = s1[1:]
        s2 = s2[:-1]
    return True
            
trunc_primes = []
i = 20

while len(trunc_primes) < 11:
    if isPrime(i) and isTruncatable(i):
        trunc_primes.append(i)
    i += 1

print (trunc_primes)
print ("Sum of the only 11 primes that are both truncatable from left to right and right to left is %d" % sum(trunc_primes))
