class Employee:
    def __init__(self, fname, lname, exp):
        self.fname = fname
        self.lname = lname
        self.exp = exp

    def __ge__(self, other):
        return self.exp >= other.exp

    def __gt__(self, other):
        return self.exp > other.exp

    def __lt__(self, other):
        return self.exp < other.exp

    def __le__(self, other):
        return self.exp <= other.exp

dept=[]
dept.append(Employee('A','A1', 10))
dept.append(Employee('B','B1', 13))

print  dept[0]>dept[1]

