from monays.dollar import Dollar

class TestMonays:
    def testMultiplication(self):
        five = Dollar(5)

        product = five.times(2)
        assert 10 == product.amount

        product = five.times(3)
        assert 15 == product.amount

    def testEquality(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))
