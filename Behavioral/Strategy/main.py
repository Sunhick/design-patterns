#!/usr/bin/python

import sys
from sortedlist import SortedList
from qsort import QuickSort
from mergesort import MergeSort
from shellsort import ShellSort


def main(*argv):
    records = SortedList(ShellSort())
    records.add('Samual')
    records.add('Jimmy')
    records.add('Sandra')
    records.add('Vivek')
    records.add('Anna')
    records.sort()

    records = SortedList(QuickSort())
    records.add('Samual')
    records.add('Jimmy')
    records.add('Sandra')
    records.add('Vivek')
    records.add('Anna')
    records.sort()

    records = SortedList(MergeSort())
    records.add('Samual')
    records.add('Jimmy')
    records.add('Sandra')
    records.add('Vivek')
    records.add('Anna')
    records.sort()

if __name__ == '__main__':
    main(sys.argv)
