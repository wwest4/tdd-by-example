class Franc:
    def __init__(self, amount):
        self._amount = amount

    def times(self, multiplicand):
        return Franc(self._amount * multiplicand)

    def equals(self, other):
        return self._amount == other._amount
