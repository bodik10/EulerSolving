from itertools import permutations

def primes():
    yield 2
    num = 3
    while True:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0: break
        else:
            yield num
        num += 1

# ----------------------------------

result = 0

def hasDivisibilityProperty(pan):
    prime = primes()
    for i in range(1, 8):
        if int(pan[i:i+3]) % next(prime) != 0:
            return False
    return True
     
for pan in permutations("0123456789"):
    if pan[0] == '0':
        continue
    panStr = "".join(pan)
    if hasDivisibilityProperty(panStr):
        print (panStr)
        result += int(panStr)

print ("The sum of all 0 to 9 pandigital numbers with divisibility property is %d" % result)
    
