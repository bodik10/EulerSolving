from itertools import islice
import myprofiler

def fib_digits():
    prev, num = 0, 1
    digits = 0
    term = 1
    while True:
        lenNum = len(str(num))
        if lenNum > digits:
            digits = lenNum
            yield term, num         # генератор повертає порядковий номер числа Фібоначі, і саме число тільки при зміні кількості цифр у числі
                                    # тобто на 25-й ітерації поверне номер числа, яке має 25 цифр
        prev, num = num, num + prev
        term += 1
    
# для переходу зразу до N-го елементу в генераторі використовується ф-я islice
# інакше потрібно було б робити список із N елементами, або
# цикл на N ітерацій, і на кожному кроці визивати __next__()

with myprofiler.profile():
    digits1000 = next( islice(fib_digits(), 999, None) )  # 1000-й елемент (1000-значне число)

print("The first term in the Fibonacci sequence to contain 1000 digits is: %dAnd 1000 digits number is:\n%d" % digits1000)

# testing
f = fib_digits()
for i in range(1,10):
    print("к-сть цифр-%d" % i, next(f))