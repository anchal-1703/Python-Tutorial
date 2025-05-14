class Math:
    def __init__(self,num):
        self.num=num
    def addtonum(self,n):
        self.num=self.num+n
    @staticmethod
    def add(a,b):
        return a+b
a=Math(5)
print(a.num)
print(a.add(5,7))
# we can pass using class name also
print(Math.add(5,7))
# to pass argument in a function without using self argument we use static method