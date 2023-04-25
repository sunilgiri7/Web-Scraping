class student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def define(self):
        return (f"name is {self.name} and age is {self.age}")
    
    # used to print the function
    def __str__(self) -> str:
        return self.define()

a = student('sunil', 21)
# a.define() # default way to print
print(a)  # with the help of def __str__ method