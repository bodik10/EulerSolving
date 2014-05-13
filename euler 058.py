def is_prime(n):
    for i in range(2, int(n**0.5 + 1)):
        if n%i == 0: return False
    return True

primes = 0

def calc_ratio(side):
    global primes
    for n in (ru, lu, ld, rd):
        if is_prime(n): primes += 1
    return primes/(side*2-1)
            
    
ru = 3    # right up diagonal in square spiral
lu = 5    # left up diagonal
ld = 7    # left down diagonal
rd = 9    # right down diagonal

side = 3

while calc_ratio(side) >= 0.1:
    side += 2
    ru = rd + side-1
    lu = ru + side-1
    ld = lu + side-1
    rd = ld + side-1
    
print (side, ru, lu, ld, rd)