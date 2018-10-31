from monays.money import Money, Bank


class TestMoney:
    def testMultiplication(self):
        assert Money.dollar(10) == Money.dollar(5).times(2)
        assert Money.dollar(15) == Money.dollar(5).times(3)
        assert Money.franc(10) == Money.franc(5).times(2)
        assert Money.franc(15) == Money.franc(5).times(3)

    def testEquality(self):
        assert Money.dollar(5) == Money.dollar(5)
        assert Money.dollar(5) != Money.dollar(6)
        assert Money.franc(5) != Money.dollar(5)

    def testCurrency(self):
        assert "USD" == Money.dollar(1).currency()
        assert "CHF" == Money.franc(1).currency()

    def testSimpleAddition(self):
        five = Money.dollar(5)
        total = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(total, 'USD')
        assert reduced == Money.dollar(10)
