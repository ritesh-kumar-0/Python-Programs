class Number:

    def __init__(self, value):
        self.value = value

    # +
    def __add__(self, other):
        return self.value + other.value

    # -
    def __sub__(self, other):
        return self.value - other.value

    # *
    def __mul__(self, other):
        return self.value * other.value


n1 = Number(20)
n2 = Number(10)

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)