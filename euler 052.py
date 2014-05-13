def is_same_digit(*items):
    digits = set(str(items[0]))
    for d in items[1:]:
        if set(str(d)) != digits: return False
    return True

i = 2
while True:
    if is_same_digit(i, i*2, i*3, i*4, i*5, i*6):
        print ("Smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits is", i)
        print (i*2, i*3, i*4, i*5, i*6)
        break
    i += 1
