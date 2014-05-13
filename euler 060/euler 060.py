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
    
primes = eval(open(r"primes_1000.txt").read())


for setOfFive in combinations(primes, 3):
    if check_set(setOfFive):
        print ("The sum for a set of %s is %d" % (setOfFive, sum(setOfFive)))
        # break

