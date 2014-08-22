import fractions, math

n, d = 428571, 1000000 # n=428571 is max n value where n/d < 3/7 when d<=1000000
n_min = math.ceil(0.428 * d)

maximum = dict(f=0, n=n, d=d)

while d >= 10:
    while n >= n_min:
        f = n/d
        if f > maximum["f"] and fractions.gcd(n, d) == 1:
            maximum = dict(f=f, n=n, d=d)
            break   # decreasing numerator is useless if you already found max proper fraction < 3/7
        n -= 1
    d -= 1
    n = math.floor(3/7 * d)         # should be 2/5 < n/d < 3/7
    n_min = math.ceil(0.4285 * d)   # I decided to increase left limit to 0.4285 (837/2000) instead of 0.4 (2/5)

print (maximum)
# {'n': 428570, 'd': 999997, 'f': 0.42857128571385716}
