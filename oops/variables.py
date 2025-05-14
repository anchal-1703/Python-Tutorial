class Employee:
    companyName="Apple" #class variable
    emplonum=0
    def __init__(self,name):
        self.emplonum+=1 #changed for only once
        Employee.emplonum+=1 #changed with every new instance
        self.name=name
        self.raise_am=0.02 #instance variable

    def showDetails(self):
        print(f"my name is {self.name} with amount {self.raise_am} from {self.companyName} sized {self.emplonum}")
# Employee.companyName="aplle" #class variable change
emp1=Employee("anchal")
emp1.raise_am=0.3 #instance variable

emp1.showDetails()
emp2=Employee("Ansh")
emp3=Employee("Anshwi")
# emp2.companyName="Google" #class variable become instance variable
emp2.showDetails()
emp3.showDetails()