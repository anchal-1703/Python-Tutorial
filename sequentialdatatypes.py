"""list comphrensions"""
# lst=[i for i in range(4)]
# print(lst)

# lst=[i*i for i in range(4)]
# print(lst)
"""conditional"""
# lst=[i*i for i in range(4) if i%2==0]
# print(lst)

"""list methods"""
lst=[]
lst.append(1)
print(lst)
lst=[20,11,4,3,8,5,9]
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
lst.reverse()
print(lst)
lst.count(3)
m=lst.copy()
print(m)
m.insert(1,22)
print(m)
m.extend(lst)
print(m)
