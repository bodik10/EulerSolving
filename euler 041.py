import myprofiler
from itertools import permutations

def isPrime(n):
    if n == 1: return False
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

def findMaxPanPrime():
    maxPan = 0
    for pre in range(7,0,-1):                           # 7 ..... . (I start with 7-digit, there are no 9 and 8-digit Pandigital prime)
        for post in [i for i in (1,3,7) if i != pre]:   # 7 ..... 1 or 3 (not 7, 'cause can be only once)
            pan = [str(i) for i in range(7,0,-1) if i != pre and i != post] # 7 [6,5,4,2,1] 1
            for perm in permutations(pan):                                  # [6,5,4,3,2], [5,6,4,3,2], [5,4,6,3,2] ...
                newPan = int("%s%s%s" % (pre, "".join(perm), post))         # 7654321
                if newPan > maxPan and isPrime(newPan):
                    maxPan = newPan
        if maxPan: 
            return maxPan
    
        
with myprofiler.profile():
    print ("The largest n-digit pandigital prime that exists is %d" % findMaxPanPrime())