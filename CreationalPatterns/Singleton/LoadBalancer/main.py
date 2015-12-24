#!/bin/python

import sys
from Utils import Log, Marker
from LoadBalancer import LoadBalancer


def main(*args):
    b1 = LoadBalancer()
    b2 = LoadBalancer()
    b3 = LoadBalancer()

    if (id(b1) == id(b2) and id(b2) == id(b3)):
        Log(Marker.Success, 'All are same instances! Singleton')
    else:
        Log(Marker.Error,
            'All are different instances! Singleton violation!!!')

    del b1, b2, b3
    balancer = LoadBalancer()
    for i in range(0, 15):
        server = balancer.Server
        Log(Marker.Debug, 'Dispatch request to {0}'.format(server))

if __name__ == '__main__':
    main(sys.argv)
