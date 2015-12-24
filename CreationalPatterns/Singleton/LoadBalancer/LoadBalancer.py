#!/bin/python

from Singleton import Singleton
from random import randint


class LoadBalancer(object):
    """
    Load balancer
    """
    __metaclass__ = Singleton

    def __init__(self):
        self._servers = ['server-1', 'server-2', 'server-3', 'server-4']

    @property
    def Server(self):
        return self._servers[randint(0, len(self._servers)-1)]
