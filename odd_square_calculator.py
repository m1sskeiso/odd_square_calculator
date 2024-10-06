class OddSquareCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_odd_squares(self):
        return [x**2 for x in self.numbers if x % 2 != 0]

# Sample usage
calculator1 = OddSquareCalculator([2, 4, 3])
print(calculator1.calculate_odd_squares())  # Output: [9]

calculator2 = OddSquareCalculator([0, 0, 1, 1])
print(calculator2.calculate_odd_squares())  # Output: [1, 1]
