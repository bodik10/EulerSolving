def pandigitalPproducts():
    result = []
    for i in range(1, 1000):
        for j in range(1, 10000):
            multiStr = str(i) + str(j)
            if len(multiStr) > 5:
                break
            productStr = (multiStr + str(i*j))
            if "0" in productStr or len(productStr) != 9:
                continue
            if len(set(productStr)) == 9:
                result.append((i, j, i*j))                
    return result

allPandigital = pandigitalPproducts()

print ("All Pandigital products:")
for p in allPandigital:
    print ("%d x %d = %d" % p)

print("Sum of all products (only uniques) whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital: %d" % sum({p[2] for p in allPandigital}))