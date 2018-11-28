class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b 
        self.c = c 

        negative = a <= 0 or b <= 0 or c <= 0
        illegal = a + b <= c or b + c <= a or c + a <= b
        if negative or illegal:
            raise ValueError('invalid Triangle dimensions')

    def type(self):
        ab = self.a == self.b
        bc = self.b == self.c
        if ab and bc:
            return 1
        elif ab or bc:
            return 2
        else:
            return 3
