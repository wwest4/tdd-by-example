class Dollar:
    def __init__(self, amount):
        self._amount = amount

    def times(self, multiplicand):
        self._amount *= multiplicand

    @property
    def amount(self):
        return self._amount

