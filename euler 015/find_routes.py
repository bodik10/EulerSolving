"""
знаходження к-сті шляхів (і координати самих шляхів) у сітці MxN (із точки 0,0 до точки MxN) методом рекурсії
"""

class Route:
    def __init__(self, width, height):
        self.w = width
        self.h = height

        self.routes = []

        self.makeRoute(0, 0) # start position (0,0)
        
    def makeRoute(self, x, y, route=[]):
        current = route[:]      # зберігається шлях для даної ітерації
        current.append((x, y))
 
        if x == self.w and y == self.h:
            self.routes.append(current)
        else:
            if x+1 <= self.w:
                self.makeRoute(x+1, y, current)
            if y+1 <= self.h:
                self.makeRoute(x, y+1, current)

    def display(self):
        return "There are %d routes through a %dx%d grid\n%s" % (
            len(self.routes),
            self.w, self.h,
            "\n".join( [ " -> ".join([repr(c) for c in route]) for route in self.routes ] )
        )

if __name__ == '__main__':
    x = Route(4, 4)
    print(x.display())
