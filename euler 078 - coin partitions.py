"Find the least value of n for which p(n) is divisible by one million."

'''
    # of ways to partition integer n
    
    Find the # of ways to partition a number
    http://www.math.temple.edu/~melkamu/html/partition.pdf
    p(<0) = 0 
    p(0) = 1
    p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + p(n-12) + p(n-15) - p(n-22) - p(n-26) + ...
        where 1,2,5,7,12... - pentagonal number k(3k-1)/2, k=[-1,1,-2,2,-3,3 ...]
    # of ways to partition n 
    p(n) = \sum_{k=1}^{\infinity} (-1)^(k+1) * { p(n-f(k)) + p(n-f(-k)) }
'''

def pentagonal(to):
    i = n = 1
    while True:
        n = i*(3*i-1)//2
        sign = -1 if i%2==0 else 1
        if n > to: break
        yield sign, n 
        i = abs(i)+1 if i<0 else -i


ways = {0: 1}            

def coin_partitions(): 
    N = 1
    while True:        
        p(N)
        if ways[N] % 1000000 == 0:
            return N, ways[N]
        N += 1

def p(N):
    global ways
    for sign, n in pentagonal(N):
        ways[N] = ways.get(N, 0) + sign * ways[N-n]
    return ways[N], ways

# testing
# for i in range(1,101): p(i)
# print(ways[5], ways [100])

print(coin_partitions())
