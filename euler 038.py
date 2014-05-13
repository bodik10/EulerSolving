import myprofiler

results = []

def isPandigital(s):
    return len(s) == len(set(s))

# 1 way
with myprofiler.profile():
    for i in range(1, 10000):
        products = []
        for j in range(1, 10):
            products.append(i*j)
            s = "".join(map(str, products))
            if s.find("0") > 0 or len(s) > 9:
                break
            elif len(s) == 9 and isPandigital(s):
                results.append( (s, i, tuple(range(1,j+1)) ))
            
print ("1 to 9 pandigital 9-digit numbers that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1:")    
results.sort(key=lambda x:x[0], reverse=True)
for res in results:
    print ("%s = %d x %s" % res)
            
            
# 2 way
with myprofiler.profile():
    maxPan = ""
    for i in range(1, 10000):
        s = ""
        for j in range(1, 10):
            s += str(i*j)
            if s.find("0") > 0 or len(s) > 9 or len(s) != len(set(s)):
                break
            elif len(s) == 9:
                if s > maxPan:
                    maxPan = s       
print (maxPan)
