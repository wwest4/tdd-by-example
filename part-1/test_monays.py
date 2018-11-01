from monays.money import Money, Bank, Sum


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
        assert "USD" == Money.dollar(1).currency
        assert "CHF" == Money.franc(1).currency

    def testSimpleAddition(self):
        five = Money.dollar(5)
        total = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(total, 'USD')
        assert reduced == Money.dollar(10)

    def testPlusReturnsSum(self):
        five = Money.dollar(5)
        total = five.plus(five)
        assert five == total.augend
        assert five == total.addend

    def testReduceSum(self):
        total = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(total, 'USD')
        assert Money.dollar(7) == result

    def testReduceMoneyDifferentCurrency(self):
        bank = Bank()
        bank.addRate('CHF', 'USD', 2)
        result = bank.reduce(Money.franc(2), 'USD')
        assert Money.dollar(1) == result

    def testIdentityRate(self):
        assert 1 == Bank().rate("USD", "USD")

    def testMixedAddition(self):
        fiveBucks = Money.dollar(5)
        tenFrancs = Money.franc(10)
        bank = Bank()
        bank.addRate('CHF', 'USD', 2)
        result = bank.reduce(fiveBucks.plus(tenFrancs), 'USD')
        assert Money.dollar(10) == result
