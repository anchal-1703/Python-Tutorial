"""kaun banega crorepati"""
ques=[
["who is the first prime minister of india:\n","jawarlal","modi","inidra gandhi","rahul",1], 
["who is the first prime minister of india:\n","jawarlal","modi","inidra gandhi","rahul",1], 
["who is the first prime minister of india:\n","jawarlal","modi","inidra gandhi","rahul",1],
["who is the first prime minister of india:\n","jawarlal","modi","inidra gandhi","rahul",1],
["who is the first prime minister of india:\n","jawarlal","modi","inidra gandhi","rahul",1]
      ]
level =[1000,2000,3000,5000,10000,20000,40000,80000,16000,32000]
# print("choose the correct answer from the below:")
# print(f"who is the first prime minister of india:\n{1 jawarlal}")
score = 0
for i in range(0,len(ques)):
    print(ques[i][0])
    print(ques[i][1:5])
    ans=int(input("choose the correct answer"))
    if(ans== ques[i][-1]):
        score= level[i]
        print(f"congratulations you won {level[i]} rupees and your score is {score}")

    else:
        score=0
        print(f"oops your answer was incorrect and your score is {score}")
        ask=input("you want to continue yes or no")
        if(ask=="yes"):
            continue
        else:
            break