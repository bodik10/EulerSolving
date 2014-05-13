from fractions import Fraction

def contToFloat(a0, period, result = 0):
    while period:
        result = 1 / (result + period.pop())
    return a0 + result

# [2; 1, 2, 1, 1, 4, 1, 1, 6] => 1264/465
def convergent(a0, contFract):
    if not contFract: return a0
    return a0 + Fraction(1, convergent(contFract[0], contFract[1:]))


if __name__ == "__main__":
    print (contToFloat(3, [7,15,1,84,6,2])) # short pi
    print (contToFloat(3, [7,15,1,292,1,1,1,2,1,3,1,14,2,1,1,2])) # pi
    print (contToFloat(3, [4,12,4]))
    print (contToFloat(2, [3,3,3,1,2,5,46,125,1,17,7]))

    e = (2, [1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1, 14, 1])
    print (contToFloat(*e)) # e
    
    print (convergent(3, [2, 2, 2]))
    print (convergent(2, [1, 2, 1, 1, 4, 1]))
