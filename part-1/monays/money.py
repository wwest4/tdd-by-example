class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def times(self, multiplicand):
        return Money(self.amount * multiplicand, self.currency)

    def equals(self, other):
        return self.amount == other.amount and self.currency is other.currency

    def plus(self, addend):
        return Sum(self, addend)

    def __eq__(self, other):
        return self.equals(other)

    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')


class Bank:
    def reduce(self, expression, currency):
        return expression.reduce(currency)


class Expression:
    pass


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, currency):
        result = self.augend.amount + self.addend.amount
        return Money(result, currency)
