def is_prime(n):
    for i in range(2, int(n**0.5 + 1)):
        if n%i == 0: return False
    return True

def count_max_digit(num):
    count = {}
    for i in num:
        count[i] = count.get(i, 0) + 1
    return [digit for digit in count if count[digit] > 1] # add to result only digits which are more than 1 in num (1112355 -> [1, 5])

def replace_digit(num, old):
    global exclude
    result = [int(num)]
    for i in [j for j in range(10) if j!=int(old)]:
        newNum = num.replace(old, str(i))
        if newNum[0] == "0": continue # skip if ***857 -> 000857 (857)
        newNum = int(newNum)
        if is_prime(newNum):
            result.append(newNum)
            exclude.append(newNum)
    return result
        
     
exclude = []

for num in range(100000, 1000000): # or (100, 1000), (1000, 10000), (10000, 100000) 
    if num in exclude or not is_prime(num):
        continue
    count = count_max_digit(str(num))
    if count:
        for digit in count:
            primes_digit_replacements = replace_digit(str(num), str(digit))
            if len(primes_digit_replacements) > 7: # could specify (>5, >3, or ==8 etc.)
                print (primes_digit_replacements)
        
# the answer is:
#    121313 [121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393]
#    *2*3*3