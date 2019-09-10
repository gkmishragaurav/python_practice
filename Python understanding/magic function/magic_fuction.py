class abc:
    def __new__(cls, *args, **kwargs):
        print 'I am the first.'
        pass

    def __init__(self, name, age):
        print 'I am 2nd'
        self.name=name
        self.age=age

    def __str__(self):
        return 'cls string.'

    def __repr__(self):
        return "<abc class - name:{0}, age:{1}>".\
            format(self.name,self.age)

    def __getattr__(self, item):
        if item == 'person':
            return(self.name, self.age)
        else:
            raise AttributeError

    # def __setattr__(self, key, value):
    #     if key == 'new_person':
    #         self.name = key
    #         self.age = 34
    #     else:
    #         super(abc, self).__setattr__(key, value)

    def __del__(self):
        print 'deletion.'

# these are class value functions used mainly for debug purpose.
a=abc('abc', 12)
print a
print str(a)
print repr(a)
a.__new__()
print(a.person1)
print repr(a)