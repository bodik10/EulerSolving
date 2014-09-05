import fractions

def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if not num % i: return False
    return True

limit = 10**6
primes = [i for i in range(2,10**6) if is_prime(i)]
result = 0

for d in range(2, limit+1):
    if d in primes:
        result += d-1
        continue
    for n in range(1, d):
        
        if fractions.gcd(n, d) == 1:
            result += 1

print(result)
