target = 200

coins = [1, 2, 5, 10, 20, 50, 100, 200]
result = [0] * (target + 1)
result[0] = 1

for coin in coins:
    for j in range(coin, target + 1):
        result[j] += result[j - coin]

for i in range(1, target+1):
    currency = ""
    if i/100>1:     currency = "£%d " % (i//100)
    if i-(100*(i//100)):  currency += "%dp " % (i-(100*(i//100)))
    
    print ("%scan be generated in %d number of ways" % (currency, result[i]))