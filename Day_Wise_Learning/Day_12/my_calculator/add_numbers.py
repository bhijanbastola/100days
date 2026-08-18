class Sum:
    def __init__(self,*numbers):
        self.numbers=numbers

    def add(self):
        return sum(self.numbers)
        