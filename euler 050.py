def is_prime(n):
    for i in range(2, int(n**0.5 + 1)):
        if n%i == 0: return False
    return True
        
primes = []
for num in range(2, 1000000):
    if is_prime(num):
        primes.append(num)

def findMaxAcceptableIndex(to):
    i = resultIndex = 1
    while sum(primes[:i]) < to:
        resultIndex = i
        i += 1
    return resultIndex

def maxPrime(to):
    end = findMaxAcceptableIndex(to) # sum from 0 to 'end' primes < to, sum more than 'end' consecutive primes > to
    currentMaxElem = 0
    
    for start in range(0, len(primes)//2):
        # change range of primes list
        while end < len(primes)-1 and sum(primes[:start]) >= primes[end + 1]:
            end += 1
            
        # break if in range left less elements than current most consecutive primes
        if len(primes[start:end]) < currentMaxElem: 
            break
        
        for offset in range(end, start, -1):
            primesSum = sum(primes[start:offset])
            if primesSum < to and is_prime(primesSum):
                if offset - start > currentMaxElem:
                    currentMaxElem = offset - start
                    result = (primesSum, start, offset, currentMaxElem)
                    break
                    
    print ("%d = primes[%d:%d] (%d elem.)" % result)

maxPrime(100)
maxPrime(1000)
maxPrime(10000)
maxPrime(100000)
maxPrime(1000000)
