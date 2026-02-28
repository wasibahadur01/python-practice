class empolyee:
    campany = "google"
    def show(self):
        print(f"the name is {self.name} and the campany is {self.campany}")

class coder():
    def __init__(self, language="python", language2="java"):
        self.language = language
        self.language2 = language2

    def getlanguage(self):
        print(F"the language is {self.language},{self.language2}")


class programmer(empolyee,coder):
    campany = "microsoft"
    def getskill(self):
        print(f"i am good in {self.language} and {self.language2}")

a=empolyee()
b=programmer()
print(a.campany,b.campany)   
b.getlanguage()
b.getskill()

