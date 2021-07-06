from functools import wraps


def decorator(fn):
    """A function that *is* a decorator. 
    Use it like so:
        @decorator
        def foobar(arg):
            return arg
    """
    @wraps(fn)
    def wrapped_fn(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapped_fn


def decorator_factory(param1, param2):
    """A function that *create* a decorator function, hence it's name: a
    factory.  Create and return a decorator taking two parameters (could be
    more).
    Use it like so:
        @decorator_factory(param)
        def foobar(arg):
            return arg
    """
    def decorator(fn):
        @wraps(fn)
        def wrapped_fn(*args, **kwargs):
            return fn(*args, **kwargs)
        return wrapped_fn
    return decorator


class Decorator(object):
    """A class that *is* a decorator.
    The function to be decorated is passed to the constructor, and the __call__
    method is called whenever the decorated function is invoked. No argument to
    this decorator. It is the class equivalent of the `decorator` function
    above.
    Note: there is no class equivalent of functools.wraps. 
    See http://stackoverflow.com/a/6394966
    """
    def __init__(self, f):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        print "Inside __init__()"
        self.f = f

    def __call__(self, *args, **kwargs):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        print "Inside __call__()"
        self.f(*args, **kwargs)
        print "After self.f(*args)"


class DecoratorFactory(object):
    """A class that *create* a decorator.
    The function to be decorated is not passed to the constructor, rather the
    arguments are. The decorator is instantiated and returned by the __call__
    method. It is the class equivalent of the `decorator_factory` above.
    Note: there is no class equivalent of functools.wraps. 
    See http://stackoverflow.com/a/6394966
    """
    def __init__(self, arg1, arg2, arg3):
        """
        Initialize a decorator factory with arguments.
        """
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        """With decorator arguments, __call__ is only called once, as part of
        the decoration process. It receive a single argument, which is the
        function object.
        """
        def wrapped_f(*args, **kwargs):
            # Decorator arguments are accessible here.
            print "Decorator arguments:", self.arg1, self.arg2, self.arg3
            f(*args, **kwargs)
        return wrapped_f
