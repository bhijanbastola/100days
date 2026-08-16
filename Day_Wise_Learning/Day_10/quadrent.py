class Quadrant:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def check(self):
        if self.x > 0 and self.y > 0:
            return f'First Quadrant ({self.x}, {self.y})'
        elif self.x < 0 and self.y >= 0:
            return f'Second Quadrant ({self.x}, {self.y})'
        elif self.x < 0 and self.y < 0:
            return f'Third Quadrant ({self.x}, {self.y})'
        elif self.x >= 0 and self.y < 0:
            return f'Fourth Quadrant ({self.x}, {self.y})'
        else:
            return f'You are at the origin ({self.x}, {self.y})'

#### Sensei Method 
    def quad(self):
        if not self.x and not  self.y:
            return f"Origin ({self.x},{self.y})"
        quadrent_mapping={
            (True,True):'first',
            (False,True):'second',
            (False,False):'Third',
            (True,False):'Fourth'


        }
        return quadrent_mapping

q=Quadrant()
print(q.quad())


