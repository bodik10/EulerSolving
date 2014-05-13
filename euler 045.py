def isPentagonal(num):
    x = (1 + (1 - 4*3*-(num*2))**0.5) / 6
    if x.is_integer():
        return int(x)
    return False

def isTriangle(num):
    x = (-1 + (1 - 4*-(num*2))**0.5) / 2
    if x.is_integer():
        return int(x)
    return False

  
for x, Hx in ((x, x*(2*x-1)) for x in range(1, 10**7)):
    xP = isPentagonal(Hx)
    xT = isTriangle(Hx)
    if xP and xT:
        print ("T(%d) = P(%d) = H(%d) = %d" % (xT, xP, x, Hx))

