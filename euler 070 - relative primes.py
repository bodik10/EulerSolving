def phi(n): # Euler's Totient function (see details in Problem 069)
    ret = 1
    i = 2
    while i*i <= n:
        p = 1
        while n%i == 0:
            p *= i
            n /= i       
        p /= i
        if p >= 1:
            ret *= p * (i-1)
        i += 1
    n -= 1
    return n*ret if n else ret

def is_perm(n1, n2):
    def countdict(n):
        return {k:n.count(k) for k in n}
    n1, n2 = str(n1), str(n2)
    return countdict(n1) == countdict(n2)

# solving problem
max, maxN, maxP = 0, 0, 0

for n in range(1,10**7):
    p = int(phi(n))
    if is_perm(n, p) and n/p > max:
        max, maxN, maxP = n/p, n, p

print ("n=%d for which φ(n)=%d is a permutation of n and n/φ(n)=%.5f is a maximum" % (maxN, maxP, max))

# The answer (after pretty long time of calculation) is:
# n=602910 for which φ(n)=120960 is a permutation of n and n/φ(n)=4.98438 is a maximum
