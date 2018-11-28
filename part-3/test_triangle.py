from triangle import Triangle

class TestTriangle:
    def testEquilateral(self):
        assert Triangle(3, 3, 3).type() == 1

    def testIsosceles(self):
        assert Triangle(3, 3, 4).type() == 2

    def testScalene(self):
        assert Triangle(3, 2, 4).type() == 3

    def testMalformed(self):
        try:
            Triangle(0, 0, 0)
            raised = False
        except ValueError as err:
            raised = True
        assert raised

        try:
            Triangle(1, 2, 3)
            raised = False
        except ValueError as err:
            raised = True
        assert raised

