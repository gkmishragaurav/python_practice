# Basic example of Builder Pattern
# Product to be made: Car
# Components: Engine, Tyres, Speedometer
# Product: Complex object to be made.
class Car():
    '''Product: Complex object to be made.'''
    def __init__(self):
        self.engine = None
        self.tyres = None
        self.speedometer = None

    def __str__(self):
        return '{} | {} | {}'.format(self.engine, self.tyres, self.speedometer)

# Abstract Builder: provides an interface to create a car object. It is abstract as it is not instantiated, only inherited by the Concrete Builder
# which uses the interface to create a car.
class AbstractBuilder():
    '''Abstract Builder: provides an interface to create a car object.'''
    def __init__(self):
        self.car = None

    def createNewCar(self):
        self.car = Car()

# Concrete Builder: inherits the Abstract Builder and implements the above interface createNewCar of the Abstract Builder class for a car object i.e. to say that
# its object is capable of creating a car by calling createNewCar() of AbstractBuilder; provides methods to create components of the product.
class ConcreteBuilder(AbstractBuilder):
    '''Concrete Builder: inherits the Abstract Builder and implements the above interface createNewCar of the Abstract Builder class for a car object i.e. to say that
       its object is capable of creating a car by calling createNewCar() of AbstractBuilder; provides methods to create components of the product.'''

    def addEngine(self):
        self.car.engine = "4-stroke"

    def addTyres(self):
        self.car.tyres = "MRF"

    def addSpeedometer(self):
        self.car.speedometer = "0-160"

# Director: in charge of building the product using an object of Concrete Builder
class Director():
    '''Director: in charge of building the product using an object of Concrete Builder'''

    def __init__(self, builder):
        self._builder = builder

    def constructCar(self):
        self._builder.createNewCar()
        self._builder.addEngine()
        self._builder.addTyres()
        self._builder.addSpeedometer()

    def getCar(self):
        return self._builder.car

concreteBuilder = ConcreteBuilder()
director = Director(concreteBuilder)

director.constructCar()
carOne = director.getCar()
print("Details of carOne:", carOne)

# ### OUTPUT ###
# Details
# of
# carOne: 4 - stroke | MRF | 0 - 160
