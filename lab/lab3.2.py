# poultry_farm.py
from chickens import RussianChicken, BelarusianChicken, MoldavianChicken

class PoultryFarm:
    def __init__(self, russian_count, belarusian_count, moldavian_count):
        self.__chicken_counts = {
            'russian': russian_count,
            'belarusian': belarusian_count,
            'moldavian': moldavian_count
        }
        self.__total_chickens = sum(self.__chicken_counts.values())
        
        self.__hens = {
            'russian': self.__create_chickens(RussianChicken, russian_count),
            'belarusian': self.__create_chickens(BelarusianChicken, belarusian_count),
            'moldavian': self.__create_chickens(MoldavianChicken, moldavian_count)
        }
        self.__total_eggs_per_month = self.__calculate_total_eggs()
    
    def __create_chickens(self, chicken_class, count):
        return [chicken_class() for _ in range(count)]
    
    def __calculate_total_eggs(self):
        return sum(
            sum(hen.get_eggs_per_month() for hen in hens) 
            for hens in self.__hens.values()
        )
    
    def get_chicken_count(self, breed):
        return self.__chicken_counts.get(breed, 0)
    
    def get_total_chickens(self):
        return self.__total_chickens
    
    def get_total_eggs_per_month(self):
        return self.__total_eggs_per_month