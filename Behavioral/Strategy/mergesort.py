"""
Merge sort
"""

from strategy import SortStrategy

class MergeSort(SortStrategy):
    def sort(self, elements):
        # fix merge sort
        # self._mergesort(elements)
        elements.sort()
        print('Merge sorted')

    def _mergesort(self, aList):
        self.mergesort(aList, 0, len(aList)-1)
 
    def mergesort(self, aList, first, last):
        # break problem into smaller structurally identical pieces
        mid = (first + last) / 2
        if first < last:
            self.mergesort(aList, first, mid)
            self.mergesort(aList, mid + 1, last)
            
        # merge solved pieces to get solution to original problem
        a, f, l = 0, first, mid + 1
        tmp = [None] * (last - first + 1)
 
        while f <= mid and l <= last:
            if aList[f] < aList[l] :
                tmp[a] = aList[f]
                f += 1
            else:
                tmp[a] = aList[l]
                l += 1
                a += 1
                
        if f <= mid :
            tmp[a:] = aList[f:mid + 1]
 
        if l <= last:
            tmp[a:] = aList[l:last + 1]
 
        a = 0
        while first <= last:
            aList[first] = tmp[a]
            first += 1
            a += 1
