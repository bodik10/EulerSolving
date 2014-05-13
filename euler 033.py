def checkNonTrivial(a, b, aCancel, bCancel):
    try:
        return a/b == aCancel/bCancel
    except:
        return False

def findCommonDigit(a, b):
    for digit in str(a):
        if digit in str(b) and digit != "0": return digit
    return False
        
for a in range (10, 98):
    for b in range(a+1, 100):
        commonDigit = findCommonDigit(a, b)
        if commonDigit:
            
            aCancel = str(a).replace(commonDigit, "", 1)
            bCancel = str(b).replace(commonDigit, "", 1)
              
            if checkNonTrivial(a, b, int(aCancel), int(bCancel)):
                print ("%d/%d = %s/%s" % (a, b, aCancel, bCancel))