a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if b == 0:
    raise ValueError("Cannot divide by zero.")
result = a / b
while True:
    user_input = input("Enter 'exit' to stop or any other value to continue: ")
    if user_input == "exit":
        break
    print("The result of", a, "divided by", b, "is:", result)