class Values:
    def __init__(self, x=0, y=0, z=0) -> None:
        self.x = abs(x)
        self.y = abs(y)
        self.z = abs(z)


    def items(self):
        return (self.x, self.y, self.z)


    def is_pythagorus_triplet(self):
        principle = (self.x ** 2) + (self.y ** 2) == (self.z ** 2)
        values = self.items()

        is_true = f"{values} is a pythagorus triplet."
        is_false = f"{values} is NOT a pythagorus triplet."

        return is_true if principle else is_false

    def product(self):
        import math
        return math.prod(self.items())


values = Values(3, 4, 5)

print(values.product())
print(values.is_pythagorus_triplet())
