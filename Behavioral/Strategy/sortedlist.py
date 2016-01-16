"""
Sorted list

"""

class SortedList(object):
    def __init__(self, sort_strategy):
        self.elems = []
        self.sort_strategy = sort_strategy

    @property
    def SortStrategy(self):
        return self.sort_strategy

    @SortStrategy.setter
    def SortStrategy(self, strategy):
        self.sort_strategy = strategy


    def add(self, element):
        self.elems.append(element)

    def sort(self):
        self.sort_strategy.sort(self.elems)
        print self.elems
