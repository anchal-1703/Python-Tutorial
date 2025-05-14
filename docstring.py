""" doc string """
def avg(a,b):
    """thi is for avg"""
    avg=a+b/2
    print(avg)
print(avg.__doc__,avg(1,5))
avg(1,3)