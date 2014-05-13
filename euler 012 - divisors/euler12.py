import myprofiler

def allDivisors(num):
    allDivs = 0
    maxDiv = num
    minDiv = 1
         
    while minDiv < maxDiv:
        
        if num % minDiv == 0:
            maxDiv = num // minDiv
            allDivs += 2
            
        minDiv += 1
       
    return allDivs
        
i = num = div = 0

with myprofiler.profile():
    
    while div <= 500:
        i += 1
        num += i
        div = allDivisors(num)

print("%dth triangle number (%d) has %d divisors" % (i, num, div))
# Answer is 76576500
# It takes ~15 sec