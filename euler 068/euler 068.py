from itertools import permutations

class Node:
    def __init__(self, value):
        self.value = value
        self.link = None
    def linkto(self, node):
        self.link = node
    def sum(self):
        return self.value + self.link.value + self.link.link.value 
    def __repr__(self):
        return "(%d) -> (%d) -> (%d)" % (self.value, self.link.value, self.link.link.value)
    
N = 3

allcomb = permutations(range(1, N*2+1))


for comb in allcomb:

    N_gon = [Node(i) for i in comb[N:]]
    outer = [Node(i) for i in comb[:N]]
    for i in range(1, N+1):
        N_gon[i-1].linkto(N_gon[i%N])
        outer[i-1].linkto(N_gon[i-1])
    sums = [node.sum() for node in outer]   # sums of each line 
    if sums[1:] == sums[:-1]:               # if sum of each line are equal
        print (sums[0], outer)

