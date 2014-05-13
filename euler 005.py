import myprofiler

counter = 0

def is_divisible(N):
    global counter
    
    for i in range(19, 1, -1):
        counter += 1
        if N % i:
            return False
    return True

def find_number():
    global counter
    
    N = 40
    while not is_divisible(N):
        N += 20
        counter += 1
    return N
        

with myprofiler.profile():
    result = find_number()

print("Smallest number that is evenly divisible by all of the numbers from 1 to 20: %d" % result) 
print (counter)
