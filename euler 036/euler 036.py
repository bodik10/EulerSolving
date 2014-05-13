def is_pelindrome(num):
    numStr = str(num)
    numBin = bin(num)[2:]
    return numStr == numStr[::-1] and numBin == numBin[::-1]

sumPelindrome = 0

import myprofiler
with myprofiler.profile():  
    
    for num in range(1, 1000000):
        if is_pelindrome(num):
            print (num, "\t", bin(num)[2:])
            sumPelindrome += num
        
print ("Sum of all numbers, less than one million, which are palindromic in base 10 and base 2 is %d" % sumPelindrome)