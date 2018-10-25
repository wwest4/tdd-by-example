class Dollar:
    def __init__(self, amount):
        self._amount = amount

    def times(self, multiplicand):
        return Dollar(self._amount * multiplicand)

    @property
    def amount(self):
        return self._amount

