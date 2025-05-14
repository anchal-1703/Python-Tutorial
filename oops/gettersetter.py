class myclass:
    def __init__(self,v):
        self.value = v #constructor
    def info(self):
        print(f"value is {self.value}")
    @property #decorator
    def ten_value(self):
        return 10* self.value
    """setter""" 
    @ten_value.setter
    def ten_value(self,new_value):
        self.value=new_value/10
        #no need to return value
    


a=myclass(10) #constructor call
print(a.value) #know the value of value
print(a.ten_value) #know the value of tenvalue
a.ten_value=50 #setter works
print(a.ten_value)
a.info()
