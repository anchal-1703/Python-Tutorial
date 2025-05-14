# a=100
# b=300 
# print("a") if a>b else print("b") if a==b else print("c")
# c= 9 if a>b else 0
# print(c)
n = int(input().strip()) 
li=[]
while n>=1: 
    rem=n%2
    q = n//2
    n=q   
    li.append(rem)
print(li)
ui=0
uix=[1]
for i in range(1,len(li)):
        if(li[i]==1):
            ui+=1
            uix.append(1)
        else:
            ui+=1
            continue      
print(len(uix))
    
