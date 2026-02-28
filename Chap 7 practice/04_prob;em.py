# num = int(input("Enter a number: "))
# for i in range(100):
#     if i % 2 ==0:       
#      print(f'{i}%{num}={i%num}')
#     else:
#          print(f'{i} is odd number')

num = int(input("Enter a number: "))

while num % 2 == 0:
 if num % 2 == 0:
    print(f'{num},is a prime number')
    break
 else:
    print(f'{num},is not a prime number')
     