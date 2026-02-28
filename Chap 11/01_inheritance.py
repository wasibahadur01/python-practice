class empolyee:
    campany = "google"
    def show(self):
        print(f"the name is {self.name} and the campany is {self.campany}")

class programmer:
    campany = "microsoft"
    def show(self):
        print(f"the name is {self.name} and the campany is {self.campany}")
    def showprog(self):
        print("i am a programmer")
a=empolyee()
b=programmer()
print(a.campany,b.campany)            