import myprofiler

perimeters = {}
maxSolutionsKey = 4
 
with myprofiler.profile():
    
    for p in range(4, 1001): # перебір периметрів від 4 (найменший можливий при цілочисельних сторонах 1,1,2) до 1000
        result = []
        for c in range(round(p/2), round(p/3), -1): # перебір гіпотенуз
            b = (p - c) - (c - 1)   # перебір катета починаючи не з 1, а з найменшого можливого при даній гіпотенузі
                                    # при P=100 і c=35, найбільший можливий катет a: a=35-1 (менший за гіпотенузу на 1), 
                                    # отже найменший можливий b: b=(100-35)-34=31
            a = p - b - c
            while a >= b: # якщо найменший катет b догнав а - перебір припиняється (бо значення b вже було як а)
                if (a**2 + b**2)**0.5 == c: # перевірка, чи є трикутник із текучими сторонами a,b,c прямокутним
                    result.append((a,b,c))
                a -= 1  # обидва катети одночасно зменшуються і збільшуються на 1 (P при цьому не міняється)
                b += 1               
        perimeters[p] = result            
        
for k in perimeters:
    if len(perimeters[k]) > len(perimeters[maxSolutionsKey]):
        maxSolutionsKey = k # значення периметра при якому є найбільше можливих прям.трикутників із цілочисельними сторонами
        
print ("For value of P = %d (P<=1000), is the number of solutions maximised:" % maxSolutionsKey, perimeters[maxSolutionsKey])
print (max([len(p) for p in perimeters.values()]))