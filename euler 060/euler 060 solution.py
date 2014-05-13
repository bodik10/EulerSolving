def is_prime(n):
    if n == 1: return True
    for i in range(2, int(n**0.5 + 1)):
        if n%i == 0: return False
    return True

primes = eval(open(r"primes_10000.txt").read())

L = len(primes)
 
px = dict() # {3: {7,11,17,..}, 7: {19,61,97,109,..}, 11: {..}.. }
pi = 1
for pi in range(L):
    p = primes[pi]
    px[p] = set()
    for qi in range(pi, L):
        q = primes[qi]
        if is_prime(int(str(p) + str(q))) and is_prime(int(str(q) + str(p))):
            px[p].add(q)
 
for xx in px:
    for axx in px[xx]:
        
        set_a = px[xx] & px[axx]
        # px[3] & px[7] -> {7,11,17,..} & {19,61,97,109,..} =
        # {673, 229, 2503, 109, 9901, 5521, 2707, 1237, 823, 4729, 541, 4159}
        # ...
        
        if len(set_a)>  0:
            for bxx in set_a:
                set_b = set_a & px[bxx]
                if len(set_b) > 0:
                    for cxx in set_b:
                        set_c = set_b & px[cxx]
                        if len(set_c)>0: print (xx, axx, bxx, cxx, set_c)

# result is: (13, 5197, 5701, 6733, 8389) = 26033
