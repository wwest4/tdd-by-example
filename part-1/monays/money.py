class Money:
    def __init__(self, amount):
        self._amount = amount

    def times(self, multiplicand):
        return self.__class__(self._amount * multiplicand)

    def equals(self, other):
        return self._amount == other._amount and self.__class__ is other.__class__
