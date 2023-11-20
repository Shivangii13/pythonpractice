class car:
    wheel = 4
    def __init__(self) -> None:
        self.mil = 10
        self.com = "BMW"
    

c1 = car()
c2 = car()

c1.mil = 8

c1.wheel = 5

print(c1.com , c1.mil , c1.wheel)
print(c2.com , c2.mil , c2.wheel)