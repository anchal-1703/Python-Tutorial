class person:
    name="anchal"
    occupation ="student"
    networth =1000
    def info(self): #self is a object for which to call a method
        print(f"{self.name} is a {self.occupation}")
a=person()
b=person()
a.name="sazia"
b.name="nazia"
a.info()
b.info()