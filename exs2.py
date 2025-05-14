import time
tr = float(time.strftime('%H.%M'))
print(tr)
if(tr > 05.00 and tr < 12.00):
    print("Good Morning!")
elif(tr > 12.00 and tr < 16.00):
    print("Good Afternoon!")
elif(tr > 16.00 and tr < 20.00):
    print("Good Evening")
elif(tr > 20.00 and tr< 05.00):
    print("Good Night")
else:
    print("Good Night")

    """ or """
    
match tr:
    case _ if(tr > 05.00 and tr < 12.00):
        print("Good Morning!")
    case _ if(tr > 12.00 and tr < 16.00):
        print("Good Afternoon!")
    case _ if(tr > 16.00 and tr < 20.00):
        print("Good Evening")
    case _ if(tr > 20.00 and tr< 05.00):
        print("Good Night")
    case _:
        print("Good Night")