class NumToWords():
    numbers = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five",
               6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
               11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen",
               16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
    decs = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    triple = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"]

    def __init__(self, number, isUseAnd=True):
        self.isUseAnd = isUseAnd
        self.number = number
        self.words = []

        self.splitNum()

    def splitNum(self): # 1234567 -> ['1', '234', '567']
        num = str(self.number)
        start = len(num) % 3
        
        triples = [num[:start]] if num[:start] else []
        for i in range(start, len(num), 3):
            triples.append(num[i:i+3])  

        self.parseToWords(triples)
        
    def parseToWords(self, triples):
        
        for i in range(len(triples)): # ['1', '234', '567'] -> for 0 to 3
            num = triples[i]
            while num:
                if num[0] == '0':   # 007
                    num = num[1:]   # 07 ->
                elif len(num) == 3:  
                    self.words.append( self.numbers[int(num[0])] )  # 346 -> three (self.numbers[3])
                    self.words.append("hundred")                    # three hundred

                    num = num[1:]                                           # 46 ->
                   
                    if int(num) and i == len(triples)-1 and self.isUseAnd:  # false if 00 or not the last triple
                        self.words.append("and")                            # three hundred and
                        
                elif int(num) in self.numbers:
                    self.words.append( self.numbers[int(num)] )     # 17 -> seventeen (self.numbers[17])
                    break
                elif len(num)==2:
                    self.words.append( self.decs[int(num[0])-2] )   # 46 -> forty (self.decs[2])
                    num = num[1:]                                   # 6 ->
                    if int(num):                # if 46 but not 40
                        self.words.append("-")  # then add '-'
                
            if int(triples[i]):
                self.words.append( self.triple[len(triples)-1 - i] ) # 12000000 -> twelve million (self.triple[2])
        
    def __str__(self):
        return " ".join(self.words).strip().replace(" - ", "-")      # ['ninety', '-', 'four'] -> ninety - four -> ninety-four
        

if __name__ == '__main__':
    for i in range(1, 101):
        x = NumToWords(i)
        print(i, "\t", str(x))
        
    x = NumToWords(20565507000015464)
    print(str(x))
