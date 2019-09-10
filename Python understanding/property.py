### understanding property in python
class Alphabet:
    def __init__(self, value):
        self._value = value

    # getting the values
    @property
    def value(self):
        print('Getting value')
        return self._value

    # setting the values
    @value.setter
    def value(self, value):
        print('Setting value to ' + value)
        self._value = value

    # deleting the values
    @value.deleter
    def value(self):
        print('Deleting value')
        del self._value

# passing the value
x = Alphabet('Peter')
print(x.value)

x.value = 'Diesel'
print(x.value)
del x.value
print(x.value)