class programmar:
    def __init__(self,name,age,language,experience,campany="palantir"):   
      self.campany=campany
      self.name=name
      self.age=age
      self.language=language
      self.experience=experience
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Programming Language: {self.language}")
        print(f"Experience: {self.experience} years")
        print(f"Company: {self.campany}")
p1 = programmar(input("Enter your name: "), int(input("Enter your age: ")), input("Enter your programming language: "), int(input("Enter your years of experience: ")))
p1.display()




        