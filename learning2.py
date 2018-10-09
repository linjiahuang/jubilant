class Foo():
    def __init__(self):
        self.counter = 1

class Bar(Foo):
    counter = 0

b = Bar()
print b.__dict__
Bar.counter = 100
print b.__dict__