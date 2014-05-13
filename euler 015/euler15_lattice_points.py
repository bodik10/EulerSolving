
"""
загальні правила знаходження к-сті шляхів у сітці MxN (із точки 0,0 до точки MxN): 

    http://www.robertdickau.com/lattices.html

суть полягає в складанні таблиці із кількістю можливих шляхів до кожної точки сітки,
після цього к-сть шляхів до точки x,y = сумі к-сті шляхів до точок (x-1,y) + (y-1,x)


Якщо сітка NxN (квадрат), то кількість можливих шляхів із точки 0,0 до точки NxN можна виррахувати за формулою:

    (2N)! / (N!)^2
    
"""

class LatticeRoute:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        
        self.points = {}    # таблиця із точками, словник у форматі {(x,y): к-сть шляхів до цієї точки, ...}
        
        for i in range(self.w + 1): self.points.setdefault((i, 0), 1)   # ініціалізація таблиці із точками
        for j in range(self.h + 1): self.points.setdefault((0, j), 1)   # перший рядок і стовпчик заповнюється одиницями 
                                                                        # (до кожної точки можливий тільки 1 шлях)

        self.makeRoutes() 
        
    def makeRoutes(self): 
        
        for x in range(1, self.w + 1):
            for y in range(1, self.h + 1):
                
                self.points[x, y] = self.points[x-1, y] + self.points[x, y-1]

    def display(self):
        return "There are %d routes through a %dx%d grid\n" % (self.points[self.w, self.h], self.w, self.h)
    
    def display_table(self):
        table = ""
            
        pointsList = [str(self.points[point]) for point in sorted(self.points)]
            
        for i in range(0, len(pointsList), self.h+1):
            table += "\t".join(pointsList[i:i + self.h+1]) + "\n\n"
        
        return table
    
        

if __name__ == '__main__':
    x = LatticeRoute(5, 10)
    print (x.display())
    print (x.display_table())
