
class computer:
   
   def __init__(self,cpu,ram) -> None:
       self.cpu =cpu
       self.ram =ram
       
   def configuration(self):
        print("config is", self.cpu,self.ram)

com1 = computer('i5',16)
com2 = computer('ryzen 3',8)

#computer.configuration(com1)
#computer.configuration(com2)

com1.configuration()
com2.configuration()