from monays.dollar import Dollar
from monays.franc import Franc
from monays.money import Money


class TestMoney:
    def testMultiplication(self):
        assert Dollar(10).equals(Dollar(5).times(2))
        assert Dollar(15).equals(Dollar(5).times(3))
        assert Franc(10).equals(Franc(5).times(2))
        assert Franc(15).equals(Franc(5).times(3))

    def testEquality(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))
        assert Franc(5).equals(Franc(5))
        assert not Franc(5).equals(Franc(6))
