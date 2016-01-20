"""
president.py

"""

from employee import Employee

class President(Employee):
    """ President """
    def __init__(self):
        super(President, self).__init__('Dick', 45000.0, 21)
