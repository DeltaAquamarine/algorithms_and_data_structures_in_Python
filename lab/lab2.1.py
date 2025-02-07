class Animal:
    def __init__(self, name, gender, age, species):
        self.name = name
        self.gender = gender
        self.age = age
        self.species = species

    def eat(self):
        print(f"{self.name} ест.")
    
    def move(self):
        print(f"{self.name} передвигается.")

class Mammal(Animal):
    def nurse_young(self):
        print(f"{self.name} кормит детёнышей.")

class Bird(Animal):
    def fly(self):
        print(f"{self.name} летит.")

class Kangaroo(Mammal):
    def __init__(self, name, gender, age, jump_height, pouch_size):
        super().__init__(name, gender, age, "Кенгуру")
        self.jump_height = jump_height
        self.pouch_size = pouch_size
    
    def jump(self):
        print(f"{self.name} прыгает на {self.jump_height} метров.")
    
    def carry_joey(self):
        print(f"{self.name} носит детёныша в сумке размером {self.pouch_size} см.")