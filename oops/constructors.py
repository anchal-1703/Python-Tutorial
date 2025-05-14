"""constructor is called automatically when an objct is created"""
# default constructor
class person:
    # def __init__(self):
    #     print("i am free")
#  parameterized constructor
    def __init__(self,name,oc):
        print("i am free")
        self.name=name
        self.occu=oc
    def info(self):
        print(f"{self.name} is a {self.occu}")


# a=person() #for default
a=person("harry","developer") #parameterized
a.info()