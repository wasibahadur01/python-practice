def temp(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = int(input("Enter temperature in Celsius: "))
fahrenheit = temp(celsius)
print(f"{celsius} degree Celsius is equal to {fahrenheit} degree Fahrenheit.")