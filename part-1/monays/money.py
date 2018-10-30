class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def times(self, multiplicand):
        return self.__class__(self._amount * multiplicand, self._currency)

    def equals(self, other):
        return self._amount == other._amount and self.__class__ is other.__class__

    def currency(self):
        return self._currency


from monays.franc import Franc
from monays.dollar import Dollar


def dollar(amount):
    return Dollar(amount, 'USD')


def franc(amount):
    return Franc(amount, 'CHF')
