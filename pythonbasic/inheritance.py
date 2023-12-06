class Employee:
    def __init__(self , name , id) -> None:
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"the name of employee:{self.id} is {self.name}")

   # class programmer(employee):
        #def showLanguage(self):
           # print("the default language is python")

e1 = Employee("Rohan Das",890)
e1.showDetails()
e2 = Employee("Rohan Das",890)
e2.showDetails()
    