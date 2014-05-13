from fractions import Fraction

# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
def ContinuedFractionE(n = 100):
    result = []
    k = 2
    while len(result) < n:
        result.extend([1, k, 1])
        k += 2
    return result[:n]

# [2; 1, 2, 1, 1, 4, 1, 1, 6] => 1264/465
def convergent(a0, contFract):
    if not contFract: return a0
    return a0 + Fraction(1, convergent(contFract[0], contFract[1:]))
    
e = (2, ContinuedFractionE())

# testing
for i in range(10):
    contFract = e[1][:i]
    conv = convergent(e[0], contFract)
    print ("%d: e= [2; %s] = %s" % (i+1, repr(contFract)[1:-1], str(conv)))


# solve the problem
e100th = convergent(2, e[1][:99])
result = sum(map(int, str(e100th.numerator)))
print ("100th convergent of the continued fraction for e:", e100th)
print ("Sum of digits in the numerator of the 100th convergent of the continued fraction for e:", result)
