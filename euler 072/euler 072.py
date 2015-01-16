import fractions

def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if not num % i: return False
    return True

def minDivisor(num):
    minDiv = 3
    while True:        
        if num % minDiv == 0:
            return minDiv    
        minDiv += 1  

hash = {}

# making hash table with 100 first element
for n in range(2, 101):
    if is_prime(n):
        hash[n] = n-1   # if n is prime number than all d/n (d<n) are reduce proper fractions
        continue
    rpf = []
    for d in range(1, n):
        if fractions.gcd(d, n) == 1:
            rpf.append(fractions.Fraction(d, n))
    hash[n] = len(rpf)
    # minDiv = minDivisor(n)
    # minDivRPF = hash[n//minDiv]
    # print ("n={0:<5} --- RPF {1:<5} n / {3:<3} ={4:<3} (RPF {5:<5} (x{6}))".format(n, len(rpf), ", ".join(map(str, rpf)), minDiv, n//minDiv, minDivRPF, len(rpf)//minDivRPF) )

result = sum(hash.values())

for n in range(101, 1000001):
    if is_prime(n):
        hash[n] = n-1
        result += n-1
        continue
    
    if n % 2 == 0:
        RPF = hash[n//2] if (n//2) % 2 != 0 else hash[n//2] * 2     # if n is even 
    else:                                                           # if n is odd (look at figure for more details)
        minDiv = minDivisor(n)
        if (n//minDiv) % minDiv == 0:
            RPF = hash[n//minDiv] * minDiv
        else:
            RPF = hash[n//minDiv] * (minDiv-1)
    result += RPF
    
    if n <= 500000:
        hash[n] = RPF

# for i in sorted(hash):
#     print ("n={0} ---> RPF {1}".format(i, hash[i]))

print (result)
