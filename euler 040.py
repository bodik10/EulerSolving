import myprofiler

def d(n):
    i = 1
    fraction = ""
    while len(fraction) < n:
        fraction += str(i) 
        i += 1
    return fraction[n-1]
 
with myprofiler.profile():
    for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        print (d(i), end=" ")


# !!! SLOW 2 way (generator)
def d_gen():
    i = 0
    while True:
        i += 1
        for digit in str(i):
            yield digit
        
with myprofiler.profile():
    fractIndex = 0
    for i in d_gen():
        fractIndex += 1
        if fractIndex in [1, 10, 100, 1000, 10000, 100000, 1000000]:
            print (i, end=" ")
        if fractIndex >= 1000000: 
            break