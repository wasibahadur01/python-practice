try:
    a = int(input("Enter a number: "))
    print("You entered:", a)    
except Exception as e:
  print("Invalid input. Please enter a valid integer.")