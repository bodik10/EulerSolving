from fractions import Fraction

def ContinuedFractionE(n = 100):
    result = [2]
    k = 2
    while len(result) < n:
        result.extend([1, k, 1])
        k += 2
    return result[:n]

def convergent(contFract):
    if len(contFract) == 1:
        return contFract[0]
    return contFract[0] + Fraction(1, convergent(contFract[1:]))
    
e = ContinuedFractionE()

e100th = convergent(e[:100])
print ( sum(map(int, str(e100th.numerator))) )
