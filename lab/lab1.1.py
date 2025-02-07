class Cat:
    def __init__(self, name, age, breed, color, weight):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
        self.weight = weight

    def meow(self):
        print(f"{self.name} мяукает: Мяу-мяу!")

    def eat(self, food):
        print(f"{self.name} ест {food}.")

    def sleep(self, hours):
        print(f"{self.name} спит {hours} часов.")


class Microphone:
    def __init__(self, brand, model, frequency_range, sensitivity, price):
        self.brand = brand
        self.model = model
        self.frequency_range = frequency_range
        self.sensitivity = sensitivity
        self.price = price

    def record(self):
        print(f"Микрофон {self.brand} {self.model} записывает звук.")

    def mute(self):
        print(f"Микрофон {self.brand} {self.model} отключен.")

    def adjust_sensitivity(self, new_sensitivity):
        self.sensitivity = new_sensitivity
        print(f"Чувствительность микрофона установлена на {self.sensitivity} дБ.")