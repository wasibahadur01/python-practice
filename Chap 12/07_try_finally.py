try :
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("The result of", a, "divided by", b, "is:", result)
except Exception as e:
    print("An error occurred:", e) 
finally:
    print("This block will always be executed, regardless of whether an exception occurred or not.")     