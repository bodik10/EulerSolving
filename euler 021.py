import myprofiler

def allDivisors(num):
    allDivsList = []
    maxDiv = num
    minDiv = 1
         
    while minDiv < maxDiv:
        if num % minDiv == 0:
            maxDiv = num // minDiv
            allDivsList.append(minDiv)
            allDivsList.append(maxDiv)
        minDiv += 1
       
    allDivsList.sort()
    return allDivsList[:-1]

def d(num):
    return sum(allDivisors(num))


result = []

with myprofiler.profile():
         
    for i in range(1, 10001):
        a = d(i)
        if a != i and i == d(a): # If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable
            result.append(i)

print("The sum of all the amicable numbers under 10000 is %d" % sum(result))
print(result)