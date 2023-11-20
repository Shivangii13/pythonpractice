class person:
    def __init__(self , n , o) -> None:
        print("hey i am devloper")
        self.name = n
        self.occ = o


    def info(self):
        print(f"{self.name} is a {self.occ}")


a = person("harry","devloper")
b = person("divya","HR")
a.info()
b.info()