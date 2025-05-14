class employee:
    def __init__(self,n,id):
        # self.__name=n #private specifier
        self._name=n #protected specifier
        self.id=id
    # def showdetails(self):
    #     # print(f"hello employee {self.name} id number is {self.id}")
    #     # print(self.name) #throw error cant exceess private like this
    #     print(self.__name)# can exceess private like this
    #     print(self.id)

    
a=employee("rahesh",1234)
a.id=23
# print(a.__name) #throw error for private specifier
print(a._employee__name) #can access private specifier
print(a.id) #can access private specifier
# a.showdetails()
        

