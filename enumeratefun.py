"""normal function"""
# marks=[12,32,43,65,7,7,5]
# index=0
# for mark in marks:
#     print(mark)
#     if index==3:
#         print("hello")
#     index+=1

"""with enumerate"""
marks=(12,32,43,65,7,7,5)

for index,mark in enumerate(marks): #by default start=0
    print(mark,index)
    if index==3:
        print("hello")

"""start from slicing"""
# marks=(12,32,43,65,7,7,5)

# for index,mark in enumerate(marks,start=1):
#     print(mark,index)
#     if index==3:
#         print("hello")
   