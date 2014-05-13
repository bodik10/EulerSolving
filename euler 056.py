maxSum = maxA = maxB = maxAB = 0

for a in range(99, 1, -1):
    for b in range(99, 1, -1):
        ab = str(a**b)
        sumAB = sum(map(int, ab))
        if sumAB > maxSum:
            maxSum = sumAB
            maxA, maxB, maxAB = a, b, ab

print ("Number %d^%d = %s has maximum digital sum (%d)" % (maxA, maxB, maxAB, maxSum))
