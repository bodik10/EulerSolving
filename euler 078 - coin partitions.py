"Find the least value of n for which p(n) is divisible by one million."

'''
    # of ways to partition integer n
    
    Find the # of ways to partition a number
    http://www.math.temple.edu/~melkamu/html/partition.pdf
    p(<0) = 0 
    p(0) = 1
    p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + p(n-12) + p(n-15) - p(n-22) - p(n-26) + ...
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
                 

def coin_partitions():
    
    target = 5

    while True:
        ways = {0: 1, 1: 0}
        
        for i in range(1, target):
            for j in range(i, target+1):
                ways[j] = ways.get(i, 0) + ways[j-i]

        # if ways[j]+1 == ways_goal:
        if (ways[target]+1) % 1000000 == 0:
            return target, ways[target]+1

        target += 1

def p(N):
    ways = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7}

    for n, sign in pentagonal(N):
        ways[N] = ways.get(N, 0) + sign * ways[N-n]

        #print(ways); input()
    return ways[N], ways

#print(coin_partitions())
#print(counting_summations(1648))

#print(counting_summations(6))

for i, j in pentagonal(50):
    print(i, j)

