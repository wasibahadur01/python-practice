def greatest(a, b, c):
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    elif(c > a and c > b):
        return c



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))  
num3 = int(input("Enter third number: "))
result = greatest(num1, num2, num3)
print(f"The greatest number among {num1}, {num2} and {num3} is {result}")