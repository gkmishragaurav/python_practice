class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __repr__(self):
        return "<Point x:{},y:{}>".format(self.x, self.y)

p1=Point(10,20)
p2=Point(10,10)
print p1, p2
p3= p1+p2
print p3
print p1-p2
print p2-p1

p1+=p2
print p1