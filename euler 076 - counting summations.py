"How many different ways can number be written as a sum of at least two positive integers?"

# much the same solution as in problem 031

def counting_summations(N):

    ways = [1] + [0]*N

    for n in range(1, N):
        for i in range(n, N+1):
            ways[i] += ways[i-n]
            print(ways); input()

    return ways[N]

print(counting_summations(5))
print(counting_summations(4))
print(counting_summations(7))
print(counting_summations(100))
