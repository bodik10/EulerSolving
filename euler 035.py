import math
import re
import myprofiler

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if not num % i:
            return False
    return True

def rotation(num): # 197 -> 719 -> 971 -> 197
    yield num
    rotatedNum = num[-1] + num[:-1]
    while rotatedNum != num:
        yield rotatedNum
        rotatedNum = rotatedNum[-1] + rotatedNum[:-1]

primes = []
for i in range(10,1000000):
    if is_prime(i):
        if not re.search("0|2|4|6|8|5", str(i)): # add to list only primes without 2,4,6,8,0 and 5
                                                 # because after rotation prime 1559 becomes 9155 and it is definetly not prime (divisible by 5)
            primes.append(i)
      
with myprofiler.profile():  
    circularPrimes = [2,3,5,7] # it's obvious
    for prime in primes:
        if prime in circularPrimes:
            continue
        temp = []
        for rotate in rotation(str(prime)):
            rotateInt = int(rotate)
            if is_prime(rotateInt):
                temp.append(rotateInt)
            else:
                break
        else:
            circularPrimes.extend(temp)

print ("There are %d circular primes below one million" % len(circularPrimes))
print (circularPrimes)
