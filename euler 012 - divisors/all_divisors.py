import myprofiler

def allDivisors(num):
    allDivs = 1
    allDivsList = [1]
    maxDiv = num
    minDiv = 2
         
    while minDiv < maxDiv:
        
        if num % minDiv == 0:
            maxDiv = num // minDiv
            
            allDivsList.append(minDiv)
            if minDiv != maxDiv: allDivsList.append(maxDiv)
            allDivs += 2
            
        minDiv += 1
       
    allDivsList.sort()
    return allDivs, allDivsList

if __name__ == '__main__':  
    num = 28122
    
    with myprofiler.profile():
        print( allDivisors(num) )
