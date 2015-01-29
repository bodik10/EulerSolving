from math import factorial as f

ftable = {i:f(i) for i in range(10)}
result = 0

for n in range(69, 1000000):
    chain = []
    term = n
    while term not in chain:
        chain.append(term)
        if len(chain) == 60:
            #print (chain)
            result += 1
            break
        term = sum (map(lambda x: ftable[int(x)], str(term)))

print (result)
