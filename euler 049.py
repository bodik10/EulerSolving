def is_prime(n):
    for i in range(2, int(n**0.5 + 1)):
        if n%i == 0: return False
    return True

# check if numbers is permutation of each other
def is_perm(*seq):
    
    def count_chars(s): # 156666554 -> {'1': 1, '5': 3, '4': 1, '6': 4}
        result = {}
        for c in str(s):
            result[c] = result.get(c, 0) + 1
        return result
    
    n = count_chars(seq[0])
    for i in seq[1:]:
        if n != count_chars(i): return False
    return True
        
primes = []
for num in range(1000, 10000):
    if is_prime(num):
        primes.append(num)

for i in range(len(primes)-2):
    for j in range(i+1, len(primes)-1):
        prime3 = primes[j] + (primes[j] - primes[i])
        if prime3 in primes and is_perm(primes[i], primes[j], prime3):
            print (primes[i], primes[j], prime3)
        
            # 1487 4817 8147
            # 2969 6299 9629

            # each of the terms increases by 3330
            # each of the three terms are prime
            # each of the 4-digit numbers are permutations of one another
            
    
