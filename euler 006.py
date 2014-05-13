a = sum(range(101))**2
b = sum(map(lambda x: x**2, range(101)))

print("%d - %d = %d" % (a , b, a - b))
