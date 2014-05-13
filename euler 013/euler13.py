numbers = [int(row) for row in open('numbers.txt')]

print( str( sum(numbers) )[:10] )