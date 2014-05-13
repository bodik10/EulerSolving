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
    
primes = eval(open(r"primes.txt").read())

# set of (733, 883, 991, 18493, 55621) 76721 - incorrect answer! so sum must be lower
# set of (7, 1237, 2341, 12409, 18433) 34427

# (3, 11, 19, 2903, 9973)

try:
    for prime1 in primes:
        for prime2 in primes[ primes.index(prime1)+1 : ]:
            if prime1 + prime2 >= 34427: break
            for prime3 in primes[ primes.index(prime2)+1 : ]:
                if sum((prime1, prime2, prime3)) >= 34427: break
                for prime4 in primes[ primes.index(prime3)+1 : ]:
                    if sum((prime1, prime2, prime3, prime4)) >= 34427: break
                    for prime5 in primes[ primes.index(prime4)+1 : ]:
                        setOfFive = prime1, prime2, prime3, prime4, prime5
                        if sum(setOfFive) >= 34427:
                            break
                        if check_set(setOfFive):
                            print ("The sum for a set of %s is %d" % (setOfFive, sum(setOfFive)))
                            raise Exception
except:
    pass
                        
                

