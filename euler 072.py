import fractions

def allDivisors(num):
    allDivsList = []
    minDiv, maxDiv = 2, num
    while minDiv < maxDiv:        
        if num % minDiv == 0:
            maxDiv = num // minDiv     
            allDivsList.append(minDiv)
            if minDiv != maxDiv: allDivsList.append(maxDiv)      
        minDiv += 1  
    allDivsList.sort()
    return allDivsList

def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if not num % i: return False
    return True

primes = [i for i in range(2,10**3) if is_prime(i)]

def reduced_proper_fraction(limit):
    result = 0
    for d in range(2, limit+1):
        if d in primes:
            result += d-1
            continue
        for n in range(1, d):     
            if fractions.gcd(n, d) == 1:
                result += 1
                

    return result

for d in range(2, 100):
    res=0
    for n in range(1, d):
        if fractions.gcd(n, d) == 1:
            res += 1
    print("n / %d -> %d" % (d, res))

#print(reduced_proper_fraction(8))
