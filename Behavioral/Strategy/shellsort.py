"""
shell sort
"""

from strategy import SortStrategy

class ShellSort(SortStrategy):
    def sort(self, elements):
        self.shellsort(elements)
        print('Shell sorted')

    def shellsort(self, array):
     "Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1."
     gap = len(array) // 2
     # loop over the gaps
     while gap > 0:
         # do the insertion sort
         for i in range(gap, len(array)):
             val = array[i]
             j = i
             while j >= gap and array[j - gap] > val:
                 array[j] = array[j - gap]
                 j -= gap
             array[j] = val
         gap //= 2
