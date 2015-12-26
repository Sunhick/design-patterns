#!/usr/bin/python

import sys
from ConfigParser import ConfigParser
from Windows import WindowsFactory
from Osx import OsxFactory
from Application import GuiApplication


def create_os_factory(os_type):
    """ create os specific factory """
    if os_type.lower() == 'osx':
        return OsxFactory()
    elif os_type.lower() == 'windows':
        return WindowsFactory()
    else:
        raise 'OS type: {os} unknown'.format(os=os_type)


def main(*argv):
    config = ConfigParser()
    config.read('defaults.cfg')
    os_type = config.get('system', 'os-type')
    factory = create_os_factory(os_type)
    app = GuiApplication(factory)
    app.run()


if __name__ == '__main__':
    main(sys.argv)
