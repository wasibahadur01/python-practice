class programmer:
    def __init__(self):
        print("i am programmer class constructor")
    
    a=3
class coder(programmer):
    def __init__(self):
        print("i am coder class constructor")
    b=4
class empolyee(coder):
    def __init__(self):
        super().__init__()
        print("i am empolyee class constructor")
    campany = "google"
    c=5
#b=programmer()
#c=coder()

a=empolyee()

print(a.a,a.b,a.c)                