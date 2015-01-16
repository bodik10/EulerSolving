high = 1000001

totients = [n for n in range(1000001)]

for i in range(2, high):
    if totients[i] == i:   # is prime
        for j in range(i, high, i):
            totients[j] -= totients[j]/i
            
print (sum(totients[2:]))
