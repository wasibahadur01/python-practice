class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Cannot divide by zero"
    def factorial(self, n):
        if n < 0:
            return "Factorial is not defined for negative numbers"
        elif n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result    
calc = calculator(10, 5)
print(calc.add())        # Output: 15
print(calc.subtract())   # Output: 5
print(calc.multiply())   # Output: 50
print(calc.divide())     # Output: 2.0
print(calc.factorial(5)) # Output: 120