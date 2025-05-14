def greet(fx):
    def mfx(*args,**kwargs):
        print("hello world")
        fx(*args,**kwargs)
        print("yesh")
    return mfx
def hello():
    print("good morning")
# @greet
def add(a,b):
    print(a+b)

greet(add)(1,6)

