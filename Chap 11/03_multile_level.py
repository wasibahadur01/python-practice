class programmer:
    a=3
class coder(programmer):
    b=4
class empolyee(coder):
    campany = "google"
    def show(self):
        print(f"the name is {self.name} and the campany is {self.campany}")
a=empolyee()
print(a.a,a.b)                