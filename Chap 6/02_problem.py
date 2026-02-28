mark1=int(input("Enter your mark1: "))
mark2=int(input("Enter your mark2: "))
mark3=int(input("Enter your mark3: "))
average=(mark1+mark2+mark3)/300*100
if average>=40:
    print("You have passed the exam",average)
else:
    print("You have failed the exam")