"How many different ways can number be written as a sum of at least two positive integers?"

# much the same solution as in problem 031

from collections import defaultdict
def find_summations(N):
    result = []
    def get_sum(set):
        return sum([num * count for num, count in set.items()])
    def summs(need, current = defaultdict(int)):
        nonlocal result
        currentSet = current.copy()
        for n in range(1, N):
            currentSum = get_sum(currentSet)
            if currentSum + n == need:  
                currentSet[n] += 1
                if currentSet not in result:
                    result.append(currentSet)
            elif currentSum + n > need:
                break  
            else:
                newSet = currentSet.copy()
                newSet[n] += 1
                summs(need, newSet)

    summs(N)
    return result

for set in find_summations(5):
    print(dict(set))

    
def counting_summations(N):

    ways = [1] + [0]*N

    for n in range(1, N):
        for i in range(n, N+1):
            ways[i] += ways[i-n]

    return ways[N]

print(counting_summations(5))
print(counting_summations(7))
print(counting_summations(100))
