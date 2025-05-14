l=[1,2,3,4,5]
newl=[]
def fil(a):
    return a<4
# newl=list(filter(fil,l))
"""or"""
newl=list(filter(lambda x:x<4,l))
print(newl)