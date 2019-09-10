__builtins__.NewnameError = LookupError
#Here Exception is super class for Myerror
class MyError(Exception):
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value

    # __str__ is to print() the value
    def __str__(self):
        return (repr(self.value))

try:
    x = 123
    if x == 123:
        raise NameError("Hi there")  # Raise Error
except (NameError, KeyError):
    print "An exception"
    raise  # To determine whether the exception was raised or not

except MyError as error:
    print "unknown123"
    raise MyError('This is new name Error')
else:
    print "unknown"
    raise NewnameError
finally:
    print("I'm finally clause, always raised !! ")