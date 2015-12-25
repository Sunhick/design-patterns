class Cook(object):
    def open_pizza(self):
        self._builder.Pizza.open()

    @property
    def Pizza(self):
        return self._builder.Pizza

    def make_pizza(self, builder):
        self._builder = builder
        self._builder.create_pizza()
        self._builder.build_dough()
        self._builder.build_sauce()
        self._builder.build_toppings()
