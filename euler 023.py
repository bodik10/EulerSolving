def sum_divisors(n):
    result = 1
    maxLeft = 2
    maxRight = n
    while maxLeft < maxRight:
        if n % maxLeft == 0:
            maxRight = n // maxLeft
            result += maxLeft
            if maxLeft != maxRight: result += maxRight
        maxLeft += 1
    return result

def check_non_abundant_sum(num):   
    for i in range(len(abundants), 0, -1):
        diff = num - abundants[i-1]
        if diff >=12 and diff in abundants:
            return True
    return False
    

abundants = []
result = 0
for i in range(1, 28123):
    if sum_divisors(i) > i:
        abundants.append(i)
    if not check_non_abundant_sum(i):
        result += i
        
print(len(abundants), abundants[:5], abundants[-5:])       
print("The sum of all the positive integers which cannot be written as the sum of two abundant numbers: %d" % result) # 4179871
