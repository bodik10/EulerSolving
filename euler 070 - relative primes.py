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

def genPrimeDESC(top):
    for n in range(top,2,-1):
        for i in range(2, int(n**0.5 + 1)):
            if n%i == 0: break
        else:
            yield n

def is_perm(n1, n2):
    def countdict(n):
        return {k:n.count(k) for k in n}
    n1, n2 = str(n1), str(n2)
    return countdict(n1) == countdict(n2)

# solving problem
min, N, P = 5, 0, 0

for n in range(10**6,10**7):
    p = int(phi(n))
    if is_perm(n, p) and n/p < min:
        min, N, P = n/p, n, p
"""
for n in genPrimeDESC(10**6):
    phi = n - 1
    if is_perm(n, phi) and n/phi < min:
        min, N, P = n/p, n, phi
"""

print ("n=%d for which φ(n)=%d is a permutation of n and n/φ(n)=%.5f is a minimum" % (N, P, min))

# The answer (after pretty long time of calculation) is:
# n=8319823 for which φ(n)=8313928 is a permutation of n and n/φ(n)=1.00071 is a minimum
