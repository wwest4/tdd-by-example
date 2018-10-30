from monays.money import Money


class TestMoney:
    def testMultiplication(self):
        assert Money.dollar(10).equals(Money.dollar(5).times(2))
        assert Money.dollar(15).equals(Money.dollar(5).times(3))
        assert Money.franc(10).equals(Money.franc(5).times(2))
        assert Money.franc(15).equals(Money.franc(5).times(3))

    def testEquality(self):
        assert Money.dollar(5).equals(Money.dollar(5))
        assert not Money.dollar(5).equals(Money.dollar(6))
        assert not Money.franc(5).equals(Money.dollar(5))

    def testCurrency(self):
        assert "USD" == Money.dollar(1).currency()
        assert "CHF" == Money.franc(1).currency()

