from fractions import Fraction
from functools import reduce

def long_division(n, d, accuracy = 100):
    decimal = str(n // d) + "."
    n %= d
    while n != 0 and len(decimal) < accuracy+1:
        n *= 10
        while n//d==0:
            n *= 10
            decimal += "0"
        if len(decimal) == accuracy+1:
            break
        decimal += str(n // d)
        n %= d

    return decimal

def CF(cf):
    if len(cf) == 1:
        return cf[0]
    return cf[0] + Fraction(1, CF(cf[1:]))

if __name__ == '__main__':
    i = 0
    result_sum = 0
    
    for row in open('CFs.txt'):
        i += 1
        
        cf_sequence = eval(row) # continued fraction sequence of squere root i
        
        if len(cf_sequence) == 1:
            continue

        # extend continued fraction (series repeat in irrational numbers)
        l = len(cf_sequence[1:])
        while len(cf_sequence) < 200:
            cf_sequence += cf_sequence[1:l+1]
        

        square_root_fraction = CF(cf_sequence)
        squere_root_decimal = long_division(square_root_fraction.numerator, square_root_fraction.denominator)
        decimal_digits_sum = reduce(lambda a, b: a + int(b), squere_root_decimal.replace('.',''), 0)

        result_sum += decimal_digits_sum

        # print(i, cf_sequence, square_root_fraction, squere_root_decimal, decimal_digits_sum); input()
        print("Square root of %d = %s. Digits sum = %d" % (i, squere_root_decimal, decimal_digits_sum))

    print(result_sum)
