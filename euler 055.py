def checkLychrel(num):
    S = num + int(str(num)[::-1])
    result = [int(str(num)[::-1]), S]
    i = 0
    while i<=50:
        if str(S) == str(S)[::-1]:
            break
        S = S + int(str(S)[::-1])
        result.append(S)
        i += 1
    else:
        return result
    return None
    
allLychrel = []

for num in range(1, 10001):
    lychrel = checkLychrel(num)
    if lychrel:
        allLychrel.append(num)

print ("There are %d Lychrel numbers below ten-thousand" % len(allLychrel))
