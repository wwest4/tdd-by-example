from monays.dollar import Dollar

class TestMonays:
    def testMultiplication(self):
        five = Dollar(5)
        assert Dollar(10).equals(five.times(2))
        assert Dollar(15).equals(five.times(3))

    def testEquality(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))
