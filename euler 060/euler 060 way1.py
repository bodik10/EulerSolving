from itertools import combinations, permutations

def is_prime(n):
    if n == 1: return True
    for i in range(2, int(n**0.5 + 1)):
        if n%i == 0: return False
    return True

def check_set(primesSet):
    primesSet = map(str, primesSet)
    for concat in permutations(primesSet, 2):
        if not is_prime( int(concat[0]+concat[1]) ):
            return False
    return True
    
primes = eval(open(r"primes_10000.txt").read())
bases  = eval(open(r"bases.txt").read())

"""
bases = []
for setOfPrimes in combinations(primes[:600], 3):
    if check_set(setOfPrimes):
        bases.append(setOfPrimes)

"""

#primes = eval(open(r"primes_10000.txt").read())
primes = eval(open(r"primes_100000.txt").read())[:3700] # <34427

try:
    for base in bases:
        for prime1 in primes[primes.index(base[-1])+1 : ]:
            if check_set(base + (prime1,)):
                
                # print (base + (prime1,))
                if sum((base + (prime1,))) >= 34427: break
                
                for prime2 in primes[primes.index(prime1)+1 : ]:
                    setOfFive = base + (prime1, prime2,)
                    if sum(setOfFive) >= 34427: break
                    
                    if check_set(setOfFive):
                        print ("The sum for a set of %s is %d" % (setOfFive, sum(setOfFive)))
                        raise Exception

except:
    pass

# The sum for a set of (733, 883, 991, 18493, 55621) is 76721
# The sum for a set of (7, 1237, 2341, 12409, 18433) is 34427
