"""with simple"""
# a=2
# b=3
# gmean=(a*b)/(a+b)
# print(gmean)

"""with function"""
# def gmean(a,b):
#     print((a*b)/(a+b))

# gmean(2,3)


"""functions with no aguments"""
# def function():
#     print("hello this is a function")

# function()

""" function with default argument"""
# def defa(a,b=1):
#     print(a*b)
# defa(5,2)
# defa(6)
"""function call be unorder"""
# defa(b=1,a=4)

"""argunments as a sequence"""
# def avg(*numbers):
#     sum=0
#     for i in numbers:
#         sum = sum + i
#     print("avg is ",sum/len(numbers))
# num = (1,2,3,4,5,6,7,8)
# avg(1,2,4,6,9)

"""argument as a dictionary"""
# def name(**name):
#     print("hello",name["fname"],name["mname"])
# name(fname = "anchanchal", mname="kulwinder")

"""function with return"""
# def avg(*numbers):
#     sum=0
#     for i in numbers:
#         sum = sum + i
#     return sum/len(numbers)
  
# c=avg(1,2,4,6,9)
# print(c)

"""factorial"""
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

def fib(n):
    for i in range(0,n):
        if(i==0):
            return 0
        elif(i==1):
            return 1
        else:
            return fib(i-2) + fib(i-1)
        
    
print(fib(1))

