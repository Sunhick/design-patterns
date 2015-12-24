#!/bin/python


class Marker(object):
    """
    Marker for console output
    """
    Success = 1
    Error = 2
    Warn = 3
    Debug = 4


class Bgcolors(object):
    """
    Background colors for console
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def Log(ltype, msg):
    """ vanila print with colors """
    if ltype == Marker.Success:
        msg = Bgcolors.OKGREEN + msg + Bgcolors.ENDC
    elif ltype == Marker.Error:
        msg = Bgcolors.FAIL + msg + Bgcolors.ENDC
    elif ltype == Marker.Debug:
        msg = Bgcolors.OKBLUE + msg + Bgcolors.ENDC

    print msg
