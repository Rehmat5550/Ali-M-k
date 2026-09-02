class Calculator:
    def add(self, a : int, b : int) -> int:
        return a + b
    def divide( self, a : int, b: int) -> float:
        return a / b

calc = Calculator()
print(calc.add(5, 3))
print(calc.divide(12, 45))
