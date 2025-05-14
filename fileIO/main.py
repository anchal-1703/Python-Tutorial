# f=open('fileIO/myfile.txt','r')














with open('fileIO/myfile.txt','r') as f:
    # print(f.read(4))
    position=f.tell()
    print("current position is at: ",position)
    f.seek(4)
    # print(f.readline())
    position=f.tell()
    print("current position is at: ",position)
    print(f.readline(5))
# i=0
# while True:
#     i+=1
#     line= f.readline()
#     if not line:
#         break
#     print(line)
# print("name:",f.name)
# print("closed:",f.closed)
# print(f.read())
# print(f.readlines())
    # m1=int(line.split(",")[0])
    # m2=line.split(",")[1]
    # m3=line.split(",")[2]
    # print(f"marks of student{i} in math{m1*2}")
    # print(f"marks of student{i} in eng{m2}")
    # print(f"marks of student{i} in sst{m3}")