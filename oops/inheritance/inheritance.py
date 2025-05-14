class employee:
    def __init__(self,n,id):
        self.name=n
        self.id=id
    def show(self):
        print(f"{self.name}'s id no. is {self.id}")

class programmer(employee):
    def showLang(self):
        print(f"the default lang is python")


e=employee("rashan",234)
e1=programmer("anchal",214)
e.show()
e1.showLang()
      