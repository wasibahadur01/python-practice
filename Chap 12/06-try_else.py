try :
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
except Exception as e:
    print("An error occurred:", e) 
else:
   print("The result of", a, "divided by", b, "is:", result)       

   

      
