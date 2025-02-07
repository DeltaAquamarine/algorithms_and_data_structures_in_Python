import math

#Родительский класс Shape
class Shape:
    def __init__(self, name):
        self.name = name  # Имя фигуры    
    #Абстрактные методы, которые будут переопределены в дочерних классах
    def area(self):
        pass  
    def perimeter(self):
        pass
    def volume(self):
        pass

#Класс Parall (параллелепипед)
class Parall(Shape):
    def __init__(self, length, width, height):
        super().__init__("Parall")
        self.length = length
        self.width = width
        self.height = height
    
    #Расчет площади поверхности
    def area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)
    
    #Расчет периметра
    def perimeter(self):
        return 4 * (self.length + self.width)
    
    #Расчет объема
    def volume(self):
        return self.length * self.width * self.height
    
    #Приватный метод для промежуточных вычислений
    def _intermediate_calculation(self):
        return self.length * self.width
    
#Класс Romb (ромб)
class Romb(Shape):
    def __init__(self, side_length, angle):
        super().__init__("Romb")
        self.__side_length = side_length
        self.__angle = angle
    
    #Геттеры для получения значений атрибутов
    def get_side_length(self):
        return self.__side_length
    
    def get_angle(self):
        return self.__angle
    
    #Сеттеры для изменения значений атрибутов
    def set_side_length(self, side_length):
        self.__side_length = side_length
    
    def set_angle(self, angle):
        self.__angle = angle
    
    def area(self):
        #Площадь ромба = a^2 * sin(угол)
        angle_rad = math.radians(self.__angle)  #Переводим угол в радианы
        return self.__side_length ** 2 * math.sin(angle_rad)
    
    #Расчет периметра
    def perimeter(self):
        return 4 * self.__side_length
    
    #Расчет объема (для ромба объем будет равен 0, так как это двумерная фигура)
    def volume(self):
        return 0
    
    #Приватный метод для промежуточных вычислений
    def _intermediate_calculation(self):
        return self.__side_length ** 2

parall = Parall(4, 5, 6)
print(f"Площадь параллелепипеда: {parall.area()}")
print(f"Периметр параллелепипеда: {parall.perimeter()}")
print(f"Объем параллелепипеда: {parall.volume()}")

romb = Romb(4, 60)
print(f"Плащадь ромба: {romb.area()}")
print(f"Периметр ромба: {romb.perimeter()}")
print(f"Объём ромба: {romb.volume()}")

# Работа с геттерами и сеттерами для второго класса:
print(f"Длина стороны ромба: {romb.get_side_length()}")
romb.set_side_length(6)
print(f"Новая длина стороны ромба: {romb.get_side_length()}")