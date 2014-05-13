from fractions import Fraction

class Myfraction(Fraction):
    def __init__(self, numerator, denominator):
        Fraction.__init__(self, numerator, denominator)

        self.maxAfterPoint = 5000
        self.int = ""
        self.noncycle = ""
        self.recur_cycle = ""
        self.makeDivision(numerator, denominator)
        
    def makeDivision(self, n, d):
        remainder = n % d
        if remainder == 0:
            self.int = str(n//d)
            return

        self.int = str(n//d)
        
        isFirstNull = True
        divBuffer = []
        while remainder != 0 and len(self.noncycle) < self.maxAfterPoint:
            while remainder / d < 1:
                self.noncycle += "" if isFirstNull else "0"
                remainder *= 10
                isFirstNull = False
            else:
                isFirstNull = True

            if remainder in divBuffer and not self.recur_cycle:
                self.recur_cycle = self.noncycle[ divBuffer.index(remainder) : ]
                self.noncycle = self.noncycle.replace(self.recur_cycle, "")
                return
            divBuffer.append(remainder)
            
            new_remainder = remainder // d
            self.noncycle += str(new_remainder)
            remainder -= new_remainder * d
    
    # 0.1666666 -> 0.1(6)        
    def toStr(self):
        if self.recur_cycle:
            return "{0}.{1}({2})".format(self.int, self.noncycle, self.recur_cycle)
        
        
    # 0.1666666 -> 0.16666666666666666666666666666666666666
    def toStrExtend(self, afterPoint = 50):
        if self.recur_cycle:
            fraction  = self.noncycle + self.recur_cycle * ((afterPoint - len(self.noncycle)) // len(self.recur_cycle))
            fraction += self.recur_cycle[ : afterPoint - len(fraction) ]

        else:
            fraction = self.noncycle[:afterPoint]
        return "{0}.{1}".format(self.int, fraction)
        

if __name__ == "__main__":
    
    for i in range(1, 11):
        x = Myfraction(1, i)
        print("1/%d=" % i, 
              x.toStrExtend(30), 
              x.toStr()
        )
          
    print(Myfraction(3, 7))
    print(Myfraction(1, 3) + Myfraction(4, 5)) # Myfraction + Myfraction = Fraction 
      
    maxRecur = Myfraction(1, 983)
    print(maxRecur.toStrExtend(2000))
    print(maxRecur.toStr())
    
    # 355/113 = 3.14... is close but not accurate irrational pi
    pi = Myfraction(355, 113)
    print(pi.toStrExtend(4000))
    print(pi.toStr())
    
    
