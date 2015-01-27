import fractions
import math

result = 0
rpf = []

for d in range(2, 12000 + 1):
    minN = math.ceil((1/3) * d)
    maxN = math.floor((1/2) * d)

    for n in range(minN, maxN + 1):
        if fractions.gcd(d, n) == 1 and 1/3 < n/d < 1/2:
            # rpf.append((n,d))
            result += 1

print (result)
