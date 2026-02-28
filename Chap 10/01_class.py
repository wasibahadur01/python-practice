class empolyee:
    def __init__(self, name, age, salary, department,skills):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department
        self.skills = skills

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Department: {self.department}, Skills: {self.skills}")

emp1 = empolyee("John Doe", 30, 50000, "IT", ["Python", "Java"])
emp1.display()