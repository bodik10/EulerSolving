import myprofiler
from collections import defaultdict

coins = [1, 2, 5, 10, 20, 50, 100, 200]
result = []
resultAll = 0

def get_sum(coins):
    return sum([num * count for num, count in coins.items()])

def coins_sums(need, current = defaultdict(int)):
    global result, resultAll
    
    currentSet = current.copy()
    
    for coin in coins:
        currentSum = get_sum(currentSet)
        if currentSum + coin == need:  
            currentSet[coin] += 1
            if currentSet not in result:
                result.append(currentSet)
                resultAll += 1
        elif currentSum + coin > need:
            break  
        else:
            newSet = currentSet.copy()
            newSet[coin] += 1
            coins_sums(need, newSet)
        

with myprofiler.profile():
    coins_sums(10)
    
print (len(result))

print (dict(result[0]))
print (dict(result[resultAll//2]))
print (dict(result[-1]))
