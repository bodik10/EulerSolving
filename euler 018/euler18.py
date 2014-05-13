# Оптимальний алгоритм, який вичисляє максимум із вершини до низу  
# але на відміну від перебору брутфорсом, не зберігає (не визначає) сам послідовний шлях (а тільки суму)

f = open("pyramide.txt", "r").readlines()
values = []
for line in f:
    temp = []
    for token in line.replace("\n", "").split(' '):
        temp.append(token)
    values.append(temp)

values.reverse()

for i in range(0, len(values) - 1):
    j = 0
    
    for k in values[i+1]:

        # можна визначити і мінімум, просто замінивши ф-цію max на min
        values[i+1][j] = max([int(k) + int(values[i][j]), int(k) + int(values[i][j+1])])
        j += 1
        
print ("Maximum total from top to bottom of the pyramide: %d" % values[len(values)-1][0])

print()
i =0
for row in values[1:]:
    i+=1
    print(row)

