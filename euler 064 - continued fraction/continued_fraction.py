def findRepeat(l):
    if not l: return l
    for i in range(1, len(l)//2+1):
        
        part = l[:i]
        
        offset = len(part)
        while offset <= len(l)-len(part):
            if part != l[offset:offset+len(part)]:
                break
            offset += len(part)
        else:
            return part

    # [1, 3, 1, 8, 1, 3, 1, 8, 1, 3, 1, 8, 1, 3] => [1, 3, 1, 8]
    # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2] => [1, 2]
    return l


def contFraction(N, max_period):
    a0 = int(N**0.5)
    repeat = []
    
    def findFraction(n, d):
        nonlocal repeat

        n, d = d, n # flip fract: 1:n/d = d/n

        # to prevent irrational in denominator:
        
        #     7      x (√N+a)     7 * (√N+a)
        #    ----             =  ------------
        #    √N-a    x (√N+a)       N - a^2
        
        numerator1 = n
        numerator2 = abs(d)
        denominator = N - d**2
        # ( nominator1 * (... + numerator2) ) / denominator
        
        if denominator == 0:
            return repeat # √4, 9, 16, 100 ....
        a = int( (numerator1 * (N**0.5 + numerator2)) / denominator )
        
        repeat.append(a)
        
        if len(repeat) < max_period:
            if numerator1 != 1:
                # 7(x-y)/14 = (x-y)/2
                denominator = denominator // numerator1
                numerator1 = 1
            numerator2 = numerator2 - a*denominator  # 1/(x) - a
            findFraction ( numerator2, denominator ) # recursion until len(repeat)==max_period
                   
    findFraction(-a0, 1)                
        
    return a0, repeat, findRepeat(repeat)

# testing
if __name__ == "__main__":
    for i in range(2,30):
        print ("\u221a%d =" % i, contFraction(i, 20))
