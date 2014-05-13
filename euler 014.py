import myprofiler

cache = [-1] * 1000000

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 (число 13 створює послідовність Колатца із 10 чисел (включаючи саме число 13))
def makeCollatz(num):
    global cache
    last = num
    count = 1   # лічильник стартує з 1 (враховується початкове число num)
    
    while last != 1:
        if last < len(cache) and cache[last-1] != -1:       # перевіряється чи є текуче число (на даній ітерації) в кеші
            cache[num-1] = count + cache[last-1] - 1        # якщо є - в кеш заноситься сума лічильника і значення із кеша (-1 - САМО ЧИСЛО ВЖЕ ПОРАХОВАНО В ЛІЧИЛЬНИКУ)
            return cache[num-1]                             # і повертається результат
        
        last = (last // 2) if (last % 2 == 0) else (3*last + 1)
        count += 1
        
    cache[num-1] = count    # занести результат в кеш
    return count

with myprofiler.profile():
    longestChain = (0,)
    
    for num in range(1, 1000000):
        chain = makeCollatz(num)
        if chain > longestChain[0]:
            longestChain = chain, num
    
    print("{1} produces the longest chain {0} with Collatz sequence".format(*longestChain))
    
    # 837799 produces the longest chain 525 with Collatz sequence