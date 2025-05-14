# def double(x):
#     return x*2
"""with lambda"""
# double=lambda x: x*2
# print(double(5))

cube=lambda x: x*x*x
print(cube(3))
avg=lambda x,y,z:(x+y+z)/3
avg(7,5,6)

"""pass function as an argument"""
def apl(fx,value):
    return 5 +fx(value)
print(apl(cube,3))
print(apl(lambda x:x**2,2))