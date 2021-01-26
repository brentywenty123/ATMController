"""
Exceptions for ATM controller.
"""

class NotValidCardError(Exception):
    pass

class NotValidPINError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass


