from math import factorial as f

for num in range(11, 100000):
    fact = [f(int(i)) for i in str(num)]
    if sum(fact) == num:
        print(num)
