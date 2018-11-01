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

    def reduce(self, bank, currency):
        rate = bank.rate(self.currency, currency)
        return Money(self.amount / rate, currency)

    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')


class Bank:
    def __init__(self):
        self.rates = {}

    def reduce(self, expression, currency):
        return expression.reduce(self, currency)

    def addRate(self, numerator, denominator, factor):
        self.rates[numerator, denominator] = factor

    def rate(self, numerator, denominator):
        return 1 if numerator == denominator else self.rates[numerator, denominator]


class Expression:
    def plus(self, addend):
        return Sum(self, addend)

    def times(self, addend):
        pass


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, currency):
        result = self.augend.reduce(bank, currency).amount + self.addend.reduce(bank, currency).amount
        return Money(result, currency)

    def plus(self, addend):
        pass
