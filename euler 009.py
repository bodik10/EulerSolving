import myprofiler

def find_c(a):
    return ( (1000-a)**2 + a**2 ) / ( 2*(1000-a) )
    
def find_triplet():
    
    for a in range(1, 333): # a < b < c (max a<=332, b<=333, c<=335)
        """
        c^2 - b^2 = a^2
        b + c = 1000 - a

        b = (1000-a) - c
        c^2 - ((1000-a) - c)^2 = a^2
        ...
        
        далі для кожного а в діапазоні методом підстановки знаходимо b i c
        і перевіряємо умову
        """
        
        c = int(find_c(a))
        b = 1000 - a - c
        
        if (a**2)+(b**2) == c**2 and a+b+c == 1000:
            return a,b,c

with myprofiler.profile():
    triplet = find_triplet()
    
print("Pythagorean triplet for which a + b + c = 1000 is", triplet)
