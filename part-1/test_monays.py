import monays.money as money


class TestMoney:
    def testMultiplication(self):
        assert money.dollar(10).equals(money.dollar(5).times(2))
        assert money.dollar(15).equals(money.dollar(5).times(3))
        assert money.franc(10).equals(money.franc(5).times(2))
        assert money.franc(15).equals(money.franc(5).times(3))

    def testEquality(self):
        assert money.dollar(5).equals(money.dollar(5))
        assert not money.dollar(5).equals(money.dollar(6))
        assert money.franc(5).equals(money.franc(5))
        assert not money.franc(5).equals(money.franc(6))
        assert not money.franc(5).equals(money.dollar(5))

    def testCurrency(self):
        assert "USD" == money.dollar(1).currency()
        assert "CHF" == money.franc(1).currency()
