class students:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def display(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.grade = input("Enter grade: ")
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
student1 = students("", 0, "")
student1.display()
student2 = students("", 0, "")
student2.display()        
