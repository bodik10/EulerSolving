from fractions import Fraction

def convergent(a0, contFract):
    if not contFract: return a0
    return a0 + Fraction(1, convergent(contFract[0], contFract[1:]))

    
def findFraction(N, n, d, repeat = []):

    n, d = d, n # flip fract: 1:n/d = d/n
    
    numerator1 = n
    numerator2 = abs(d)
    denominator = N - d**2

    a = int( (numerator1 * (N**0.5 + numerator2)) / denominator )
    
    repeat = repeat[:]
    repeat.append(a)
    yield repeat

    if numerator1 != 1:
        denominator = denominator // numerator1
        numerator1 = 1
    numerator2 = numerator2 - a*denominator 

    for x in findFraction ( N, numerator2, denominator, repeat ):
        yield x                         # http://stackoverflow.com/questions/8991840/recursion-using-yield
#       yield from findFraction(...)    # only in Python 3.3
                        

result = {}

squares = [i**2 for i in range(2,32)]
for D in range(2, 1001):
    if D in squares: continue
    
    a0 = int(D**0.5)
    for cont in findFraction(D, -a0, 1):
        xy = convergent(a0, cont)
        if xy.numerator**2 - D * xy.denominator**2 == 1:
            result[D] = xy
            break
    else:
        result[D] = None
    
# print (result)
sorted_result = list(result.keys())
sorted_result.sort(key = lambda x: result[x].numerator, reverse = True)
print ("The largest x=%d is obtained when D=%d" % (result[sorted_result[0]].numerator, sorted_result[0]))
    