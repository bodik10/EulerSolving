from continued_fraction import contFraction

odd_count = 0

for N in range(2,10001):
    cont_fract = contFraction(N, 500) # find square root of N
    
    # if has an odd period
    if len(cont_fract[2]) > 0 and len(cont_fract[2])%2 == 1:
        odd_count += 1

print ("There are %d continued fractions for N≤10000 have an odd period" % odd_count)

