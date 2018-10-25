class TestMonays:
    def testMultiplication(self):
        five = Dollar(5)
        five.times(2)
        assert 10 == five.amount
