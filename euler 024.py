from itertools import permutations, islice

# для переходу зразу до N-го елементу в генераторі використовується ф-я islice
# інакше потрібно було б робити список із N елементами, або
# цикл на N ітерацій, і на кожному кроці визивати __next__()

millionth = next( islice(permutations(range(10)), 999999, None) )
millionth = list(map(str, millionth))

print(
    "Millionth lexicographic permutation of the digits 0,1,2,3,4,5,6,7,8,9 is %s" %  
    "".join(millionth)
)
