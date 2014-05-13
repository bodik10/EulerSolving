from fractions import Fraction

# 3.124 => 124, 1000
def get_decimal(f):
    if not isinstance(f, float) or f.is_integer():
        return False
    decimal = str(f).split(".")[1]  # '124'
    return int(decimal), 10**len(decimal)

# works only with RATIONAL fractions (e.g. 1.25, 3.7455 but NOT √2, √10, etc)

# 3.124 => 3, [8, 15, 2]
def cont_fract(f):
    a0 = int(f)
    repeat = []
    n, d = get_decimal(f)
    fract = Fraction(n, d)
    while fract: # end of cont.fract if 3/1 - 3 = Fraction(0,1)
        fract = 1 / fract
        a = int(fract)
        repeat.append(a)
        fract = fract - a
        
    return a0, repeat
    
if __name__ == "__main__":
    print (cont_fract(1.125))
    print (cont_fract(3.124))
    print (cont_fract(7.5))
    print (cont_fract(2.7755145))
    print (cont_fract(1.4142136248)) # ~√2, should be [1; (2)]
