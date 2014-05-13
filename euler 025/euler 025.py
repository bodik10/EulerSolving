import myprofiler

with myprofiler.profile():
    a, b = 1, 1
    icount = 2
    fib = 1
    
    while len(str(fib)) != 1000:
        fib = a + b
        a = b
        b = fib
        icount += 1
    
    print(icount)
