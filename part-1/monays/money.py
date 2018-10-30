class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def times(self, multiplicand):
        return Money(self._amount * multiplicand, self._currency)

    def equals(self, other):
        return self._amount == other._amount and self.currency() is other.currency()

    def currency(self):
        return self._currency


    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')
