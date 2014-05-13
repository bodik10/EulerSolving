res = 0

for i in range(1, 10):
    for n in range(1, 100):
        P = i**n
        if len(str(P)) > n: break
        if len(str(P)) == n:
            res += 1
            print ("%d^%d = %d (%d digit)" % (i, n, P, n))

print ("There are %d n-digit positive integers which are also an nth power" % res)
