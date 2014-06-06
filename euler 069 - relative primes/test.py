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
        
    return n-1 if n*ret else ret

for n in range(2, 20):
    print (n, phi(n))
