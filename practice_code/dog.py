class Dog :
    def __init__ (self, initialname, age=0):
        self.name = initialname
        self.age = age
    def speak(self):
        print(self.name + " says Rrrrufffff!")
    def change_name(self, new_name):
        self.name = new_name

    def calculate_dog_years(self):
        return self.age * 7
    def celebrate_birthday(self):
        self.age += 1
        print("Happy Birthday " + self.name)
bingo = Dog("bingo", 3)
bingo.speak()
bingo.change_name("fido")
rex = Dog("rex", 0)
rex.speak()
thor = Dog("thor", 11)

bingo.celebrate_birthday()
rex.celebrate_birthday()
thor.celebrate_birthday()

