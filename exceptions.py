# try:
#     a=int(input("enter a number"))
#     print(f"multiplication of {a} is")
#     for i in range(1,11):
#         print(f"{i} * {a} ={i*a}")
# except ValueError:
#     print("invalid error occured")
# except IndexError:
#     print("ivalid")

"""finally used in function  """
# def fun():
#     try:
#         l=int(input("enter index of "))
#         lst=[2,3,6,8]
#         print(lst[l])
#         return 1
#     except:
#         print("error occured")
#         return 0
#     finally:
#         print("hello i always execute")
# fun()
"""raise error"""

# a=int(input("enter value between 5 and 8"))

# if(a<5 or a >8):
#     raise ValueError("eneter num between 5 and 8 only")

"""importing sys"""
import sys
print(sys.exc_info()[0])

try:
    a=int(input("enetr a num"))
    r=1/a
   
except:
    print(sys.exc_info()[1],"occured")
    print("try again")

"""customized exception"""
# class invalidAge(Exception):
#     print("invalid")
#     pass
# a=5
# try:
#     if a>18:
#         print("right to vote")
#     else:
#         raise invalidAge 
# except invalidAge:
#     print("invalid")