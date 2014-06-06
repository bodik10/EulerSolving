def phi(n):
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

# solving problem
max, maxN = 0, 0

for n in range(2,1000001):
    φ = phi(n)
    if n/φ > max:
        max, maxN = n/φ, n

print ("n=%d for which n/φ(n)=%.5f is a maximum" % (maxN, max))
