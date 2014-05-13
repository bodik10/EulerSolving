primes = []

def is_prime(N):
    for i in range(2, int(N**0.5) + 1):
        if N%i==0:
            return False
    return True

i=2
while len(primes) < 10001:
    if is_prime(i):
        primes.append(i)
    i += 1

print("10 001st prime number is %d" % primes[-1])
