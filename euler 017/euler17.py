from numtowords import NumToWords

sum = 0
for i in range(1, 1001):
    x = NumToWords(i)
    sum += len(str(x).replace(" ", "").replace("-", ""))
    
print("Numbers from 1 to 1000 written out in words used %d letters" % sum)