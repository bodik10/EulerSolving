import myprofiler

rang = range(999,99,-1)

def find_palindrome():
    result = []
    counter = 0
    
    for i in rang:
        for j in rang:
            palinNum = i*j
            counter += 1

            if str(palinNum) == str(palinNum)[::-1]:
                result.append((i, j, palinNum))

    print("Iterations:", counter)
    return result


with myprofiler.profile():
    l = find_palindrome()
    l.sort(key=lambda x: x[2])

print("Largest palindrome made from the product of %dx%d: %d" % l[-1]) 
