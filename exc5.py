import random 

# print("snake") if com==1 else print("water") if com==2 else print("gun")

# print("congratulations! you won") if (com == 1 and player==3) or (com==2 and player==1) or (com==3 and player==2) else print("its a draw") if (com==player) else print("oops! you lost")
# game=[[0,1,2],[0,1,2],[0,1,2]]
# player=int(input("1.Snake\n2.Water\n3.gun\nchoose one of the above"))
# for i in range(len(game)):
def check(com,user):
    if com==user:
        return 1
    elif (com ==3 and user == 1) or (com==1 and user == 2) or

player=int(input("1.Snake\n2.Water\n3.gun\nchoose one of the above"))
score=random.randint(1,3)
     