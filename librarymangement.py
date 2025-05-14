# Borrow a book (remove it from available books).
# • Return a book (add it back to available books).
# • View all available books.
# • Use functions for borrowing, returning, and viewing books, with proper error
# handling (e.g., if a user tries to borrow a book that’s already taken).
class library:
    books={"Pride and Prejudice" :"Jane Austen","1984" :"George Orwell","Crime and Punishment" :"Fyodor Dostoevsky","Hamlet" :" William Shakespeare","One Hundred Years of Solitude" :"Gabriel García Márquez"}
    x=list(books.keys())
    y=list(books.values())
    def availableBooks(self):
        
        print("Available books are:")
        for i in range(0,len(self.x)):
            print(f"{i+1}: {self.x[i]} by {self.y[i]}")
    def borrowBooks(self,choice,name):
        try:
            print(len(self.x))
            if choice <= len(self.x):
                print(self.x[choice])
                self.x.pop(self.x[choice-1])
                self.y.pop(self.y[choice-1])
                print(f"{self.x[choice-1]} by {self.y[choice-1]} is being issued to {name}")
            # else:
            #     print("please selected the books from the avaliable list")
        except:
            print("select appropriate choice from the give books")
    
a=library()
choice=int(input("please select one of these"))
if choice == 2:
    bor=int(input("enter the book you want to borrow"))
    name=input("enter your name")
    a.borrowBooks(bor,name)
# a.availableBooks()
