import re
pattern ="[A-Z|a-z]hoes"
text="i want to shoes wash my shoes 24"
# print(re.search(pattern,text))
# print(re.findall(pattern,text))
print(re.findall("sh*",text))
print(re.findall("sh+",text))
# x=re.match(pattern,text)
# print(x)
# x=re.search(pattern,text)
# if x:
#     print("match")
# else:
#     print("no match")
# x=re.sub(pattern,"anchal",text,1)
# x=re.split("\s",text)
# print(x)
