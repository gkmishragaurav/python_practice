class ObjectFactory:
    def __init__(self):
        self._builder = {}

    def register_builder(self, key, builder):
        '''Registering a builder, respective key will be added to private _builder'''
        self._builder[key] = builder

    def get(self, key, **kwargs):
        '''getting the registered value from builder.'''
        builder = self._builder.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)