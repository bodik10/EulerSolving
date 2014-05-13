from math import factorial as f

def all_ways(n, r):
    return f(n)/(f(r)*f(n-r))    

result = 0
for n in range(23,101):
    for r in range(2, n//2 + 1):
        if all_ways(n, r) >= 1000000:
            result += 1 if n%2==0 else 2 # if n is odd  C(nr)=[a,b,c,c,b,a] -2 max in the middle
                                         # if n is even C(nr)=[a,b,c,b,a] -1 max in the middle
            result += (n//2-r) * 2
            break

print ("There are %d values of  C(nr), for 1 ≤ n ≤ 100, are greater than one-million" % result)
