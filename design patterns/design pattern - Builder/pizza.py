class Pizza:
    def __init__(self):
        self.sauce = None
        self.toppings=None
        self.dough=None

class BasePizzamaker:
    def __init__(self):
        self.pizza = None
        self.state = 'queued'
        self.bakig_time = 5

    def make_pizza(self):
        self.pizza = Pizza()

    def prepare_dough(self):
        self.state = 'preperation'
        print self.state

    def bake(self):
        self.state = 'baking'
        print self.state

class MargaritaPizzaMaker(BasePizzamaker):
    def add_dough(self, dough='thin'):
        print 'making crust'
        self.pizza.dough = dough

    def add_sauce(self, sauce='tomato'):
        print 'adding sauce'
        self.pizza.sauce = sauce

    def add_toppings(self, toppings=['cheez']):
        print 'adding toppings'
        self.pizza.toppings= toppings

class waiter:
    def __init__(self, builder):
        self._builder = builder

    def makePizza(self):
        steps = [self._builder.make_pizza,
                 self._builder.prepare_dough,
                 self._builder.add_dough,
                 self._builder.add_sauce,
                 self._builder.add_toppings,
                 self._builder.bake]
        [step() for step in steps]

    @property
    def pizza(self):
        return self._builder.pizza.dough, 'crust', \
               self._builder.pizza.sauce, \
               self._builder.pizza.toppings

pzb = MargaritaPizzaMaker()
w = waiter(pzb)
w.makePizza()
print 'final pizza = ', w.pizza