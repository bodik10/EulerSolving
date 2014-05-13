import myprofiler

def digitsPower(power, num):
    digits = [int(digit)**power for digit in str(num)]
    return sum(digits)

numbers = []

with myprofiler.profile():
    for num in range(2, 6*9**5):
        if num == digitsPower(5, num):
            numbers.append(num)
    
print (numbers)
print ("Sum of all the numbers that can be written as the sum of fifth powers of their digits: %d" % sum(numbers))