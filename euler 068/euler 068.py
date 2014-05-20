from itertools import permutations

class Node:
    def __init__(self, value):
        self.value = value
        self.link = None
    def linkto(self, node):
        self.link = node
    def sum(self):
        return self.value + self.link.value + self.link.link.value
    def toTuple(self):
        return (self.value, self.link.value, self.link.link.value)
    def toStr(self):
        return "".join(map(str, self.toTuple()))
    def __repr__(self):
        return "(%d) -> (%d) -> (%d)" % (self.value, self.link.value, self.link.link.value)

def isUnique(target, collect):
    if target in collect:
        return False
    for l in collect:
        for i in range(len(l)):
            if target == l[i:] + l[:i]: return False
    return True

def concat_group(groups):
    result = []
    for group in groups:
        concat = "".join(group)
        result.append(int(concat) if len(concat)!=17 else 0)
    return max(result)
        
# N = 3 # testing   
N = 5

result = {}

for comb in permutations(range(1, N*2+1)):

    N_gon = [Node(i) for i in comb[N:]]
    outer = [Node(i) for i in comb[:N]]
    for i in range(1, N+1):
        N_gon[i-1].linkto(N_gon[i%N])
        outer[i-1].linkto(N_gon[i-1])
    sums = [node.sum() for node in outer]

    if len(set(sums)) == 1:
        # group = [node.toTuple() for node in outer]
        group = [node.toStr() for node in outer]
        
        if sums[0] not in result:
            result[sums[0]] = []
        
        if isUnique(group, result[sums[0]]):
            result[sums[0]].append(group)

maximum = 0

for sums, group in result.items():
    print (sums, group) # testing
    
    concat = concat_group(group)
    if concat > maximum:
        maximum = concat

print ("Maximun string for a 'magic' %d-gon: %d" % (N, maximum))
