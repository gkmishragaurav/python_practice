# This is implementation for a reverse range function - iterator function.

class MyIterator(object):
     def __init__(self, step):
         self.step = step

     def next(self):
         """Returns the next element. Stop when step is 0"""
         if self.step == 0:
             raise StopIteration
         self.step -= 1
         return self.step

     def __iter__(self):
         """Returns the iterator itself."""
         return self

for el in MyIterator(4):
    print el

# range function using yeald - generator function.
def my_range(num):
    i=0
    while(i<num):
        yield i
        i=i+1

for x in my_range(4):
    print x