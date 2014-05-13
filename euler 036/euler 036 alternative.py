def is_pelindrome(num, base):
    reversed = 0
    k = num
    while k > 0:
        reversed = (base * reversed) + (k % base)
        k = k // base
    return num == reversed

sumPelindrome = 0

import myprofiler
with myprofiler.profile():  
    
    for num in range(1, 1000000, 2):   # It is easy to see that a number in base 2 must be odd to be a palindrome
        if is_pelindrome(num, 2) and is_pelindrome(num, 10):
            print (num, "\t", bin(num)[2:])
            sumPelindrome += num
        
print ("Sum of all numbers, less than one million, which are palindromic in base 10 and base 2 is %d" % sumPelindrome)