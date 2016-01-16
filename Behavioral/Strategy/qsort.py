"""
Quick sort
"""

from strategy import SortStrategy

class QuickSort(SortStrategy):
    def sort(self, elements):
        # Fix quick sort
        # self.quicksort(elements, 0, len(elements)-1)
        elements.sort()
        print('Quick sorted')

    def quicksort(self, alist, first, last):
        if first < last:
            splitpoint = self.partition(alist, first, last)
            self.quicksort(alist, first, splitpoint-1)
            self.quicksort(alist, splitpoint+1, last)


    def partition(self, alist, first, last):
        pivotvalue = alist[first]

        leftmark = first+1
        rightmark = last

        done = False
        while not done:
            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1
