import time  #Импортируем модуль time для измерения времени выполнения функции

#Определяем декоратор, который измеряет время выполнения функции
def timing_decorator(func):
    def wrapper(*args, **kwargs):  #Принимает любые аргументы
        start_time = time.time()  #Время начала
        result = func(*args, **kwargs)  #Вызываем исходную функцию и сохраняем результат
        end_time = time.time()  #Время окончания
        execution_time = end_time - start_time  #Вычисляем разницу
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")  
        return result  #Возвращаем результат
    return wrapper  #Возвращаем обёрнутую функцию

#Определяем функцию, выполнение которой займёт 2 секунды
def example_function():
    time.sleep(2)  #Имитация задержки
    print("Function execution finished")

#Применяем декоратор вручную
example_function = timing_decorator(example_function)

#Вызываем функцию
example_function()
