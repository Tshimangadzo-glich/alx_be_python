class SimpleCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
["SimpleCalculator()"]

["import", "unittest", "from simple_calculator"]

["test_addition", " self.assertEqual(self.calc.add", "test_addition(self)"]

["test_subtraction", " self.assertEqual(self.calc.subtract", "test_subtraction(self)"]
