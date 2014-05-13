def fibonacci(prev=0, last=1):
    
    while last <= 4000000:
        
        sumF = prev + last

        prev, last = last, sumF
        
        yield sumF



f_even=[]
sum_even = 0

for i in fibonacci():
    print(i)    # all fibonacci numbers
    
    if not i%2: # only even 
        sum_even += i

print ("Answer is: %d" % sum_even)
    

