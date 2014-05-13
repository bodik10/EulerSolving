from collections import defaultdict

def is_triangle(P):
    n = (-1 + (1+8*P)**0.5) / 2
    return n.is_integer(), n

def is_square(P):
    n = P**0.5
    return n.is_integer(), n

def is_pentagonal(P):
    n = (1 + (1+24*P)**0.5) / 6
    return n.is_integer(), n

def is_hexagonal(P):
    n = (1 + (1+8*P)**0.5) / 4
    return n.is_integer(), n

def is_heptagonal(P):
    n = (3 + (9+40*P)**0.5) / 10
    return n.is_integer(), n

def is_octagonal(P):
    n = (2 + (4+12*P)**0.5) / 6
    return n.is_integer(), n

# for which each polygonal type (triangle, square, pentagonal, hexagonal, heptagonal, and octagonal)
# is represented by a different number in the set
def is_different(chain):
    polygonal_set = set()
    for link in sorted(chain, key=lambda x: len(sets[x])): # move list with more than 1 polygonal to end
                                                           # chain = [1281, 8128, 2882, 8256, 5625, 2512] -> [[8], [3, 6], [5], [3], [4], [7]]
                                                           # after sort: [1281, 2882, 8256, 5625, 2512, 8128] -> [[8], [5], [3], [4], [7], [3, 6]]
        if len(sets[link])==1 and sets[link][0] in polygonal_set: return False
        polygonal_set.update(sets[link])

    return polygonal_set == {3,4,5,6,7,8}

def find_chain(chain):
    if len(chain) == 6:                                 # set of six
        if str(chain[0])[:2] == str(chain[-1])[-2:]:    # cyclic
            if is_different(chain):                     # represented by a different number in the set
                print (chain)                           # RESULT
    elif len(chain) > 6:    
        return False
    
    end = str(chain[-1])[-2:]
    links = list(filter(lambda x: str(x)[0:2]==end and x not in chain, sets.keys()))
   
    for link in links:
        current_chain = chain[:]
        current_chain.append(link)
        find_chain(current_chain)

sets = defaultdict(list)

figurate = {3: is_triangle, 4: is_square, 5: is_pentagonal, 6: is_hexagonal, 7: is_heptagonal, 8: is_octagonal}

for n in range(1000, 10000):
    for fname, f in figurate.items():
        if f(n)[0]:
            sets[n].append(fname)

for N in sets:
    next_chain_link = find_chain([N])

"""
RESULT IS:
[1281,
   8128,
     2882,
       8256,
         5625,
           2512]
             1281
               ...
"""
