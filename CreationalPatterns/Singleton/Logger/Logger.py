#!/usr/bin/python

import os
import multiprocessing
from datetime import datetime
from Singleton import Singleton


class LogManager(object):
    """
    Logger Manager

    returns a singleton instace of logger
    """
    @staticmethod
    def get_logger():
        return Logger()


class Logger(object):
    """
    Logger class.

    Dumps the logs to a file with <processname>_<pid>_<time>.txt
    """
    __metaclass__ = Singleton

    def __init__(self):
        try:
            self.pid = os.getpid()
            filename = '{pname}_{pid}_{time}.txt'.format(
                pname=multiprocessing.current_process().name,
                pid=str(self.pid), time=datetime.now())
            self.logfile = open(filename, 'w')
        except Exception:
            print('Error in opening file')
            raise Exception

    def log(self, logtype, msg):
        self.logfile.write('{tstamp} {pid} {logtype} {text}\n'.format(
            tstamp=datetime.now(), logtype=str(logtype),
            text=msg, pid=self.pid))

    def __del__(self):
        self.logfile.close()
