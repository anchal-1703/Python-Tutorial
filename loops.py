"""for loop"""

# a = "anchal"
# for i in a:
#     print(i,end=", ")

# list = ["red", "green", "blue"]
# for color in list:
#     print(color)
#     for i in color:
#         print(i)

"""range fn in for loop"""

# for i in range(1,9,2):
#     print(i)


""" while loop"""
# i=0
# while i <10:
#     print(i+2)
#     i+=1

# while i <10:
#     print(i)
#     if i==2:
#         print(i)
#     i+=1

# while i <10:
#     i = int(input("enter a number"))
#     i+=1

"""decrementing loop"""
# i=10
# while i >0:
#     print(i,end=" ")
#     i-=1

# i=0
# lis = []
# while i <10:
#     n = int(input("enter a number"))
#     lis.append(n)
#     i+=1
# print(lis)
# print(max(lis))
# print(min(lis))

"""while else"""
# i=11
# while i <10:
#     print(i)
#     i+=1
# else:
#     print("end of the loop")

"""break statements"""
# for i in range(1,12):
#     if(i==10):
#         break
#     print('5 *',i,'=',5*i)
# print("break says \"get out of the loop\"")

# i=1
# while i<12:
#     if(i==10):
#         break
#     print('5 *',i,'=',5*i)
#     i+=1
# print("break says \"get out of the loop\"")

"""Continue statement"""
# for i in range(1,12):
#     if(i==10):
#         print("continue says \"skip the iterartion\"")
#         continue
#     print('5 *',i,'=',5*i)


"""produce infinite loop"""

# i=1
# while i<12:
#     if(i==10):
#         print("continue says \"skip the iterartion\"")
#         continue
#     print('5 *',i,'=',5*i)
#     i+=1


"""produce correct answer"""
# i=0
# while i<12:
#     i+=1
#     if(i==10):
#         print("continue says \"skip the iterartion\"")
#         continue
#     print('5 *',i,'=',5*i)

"""enuminate DO-WHILE by using infinite loop"""

# i=0
# while True:
#     print(i)
#     i+=1
#     if(i%5==0):
#         break

#     """for with else"""
# for i in range(1,10):
#     print("i dont like {}".format(i))
#     # if i==6:
#     #     break
# else:
#     print("no i")
 


"""while loop"""
# intialization
# while(condition):
#     //statement
#     increment  decrement

i=1 #start
while(i<10): #end
    
    i+=1 #step
    
# wap to print the sum of first 10 natural numbers

# wap to print the factorial of a given number input by the user
# 1,2,3,4,5,6,7,8,9,10
# sum=0 +i when i =1
# sum=1 +i whe i=2 sum=3
# i=3 sum=6
# i=4 sum=10
# i=5 sum=15
# i=6 sum=21
# i=7 sum=28
# i=8 sum =36
# i=9 sum 45
# i=10 sum 55
# i=11 condition break


i=1
sum=0
while(i<=10):
    sum=sum+i
    print("i = ",i,"sum=",sum)
    i+=1
print(sum) 


