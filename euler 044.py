from itertools import combinations

def isPentagonal(num):
    x = (1 + (1 - 4*3*-(num*2))**0.5) / 6
    if x.is_integer():
        return int(x)
    return False

def P(x):
    return int( x * (3 * x - 1) / 2 )

# alternative way - through combinations:
# allNums = [ for n in range(1,3000)]
# for i, j in combinations(allNums, 2):

for i in range(2, 3000): # 3000 set after result to prevent long calculation (was 10000)
    for j in range(i, 0, -1):
        
        p1, p2 = P(i), P(j)
        if isPentagonal(p1 + p2) and isPentagonal(abs(p1 - p2)):
            
            print ("""
P({2}) = {0}
P({3}) = {1}
P({2}) + P({3}) = {4} is P({6})
|P({2}) - P({3})| = {5} (this is the answer) is P({7})""".format(p1, p2, i, j, p1+p2, abs(p1-p2), isPentagonal(p1+p2), isPentagonal(abs(p1-p2))) )


