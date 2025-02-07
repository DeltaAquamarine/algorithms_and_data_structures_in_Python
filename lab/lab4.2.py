class Branch:
    _branches = []  #Закрытый список всех филиалов
    
    def __init__(self, name, employees, revenue, expenses):
        #Инициализация атрибутов для каждого филиала
        self.name = name  #Название
        self.employees = employees  #Количество сотрудников
        self.revenue = revenue  #Доход
        self.expenses = expenses  #Расходы
        Branch._branches.append(self)  #Добавление филиала в общий список
    
    def update_revenue(self, amount, increase=True):
        #Увеличение или уменьшение дохода
        self.revenue += amount if increase else -amount
    
    def update_expenses(self, amount, increase=True):
        #Увеличение или уменьшение расходов
        self.expenses += amount if increase else -amount
    
    def _calculate_profit(self):
        #Вычисление прибыли как разницы между доходами и расходами
        return self.revenue - self.expenses
    
    def present(self):
        profit = self._calculate_profit()  #Вызов приватного метода для вычисления прибыли
        #Формирование строки с данными
        return (f"Филиал: {self.name}\n"
                f"Сотрудников: {self.employees}\n"
                f"Доход: {self.revenue}\n"
                f"Расходы: {self.expenses}\n"
                f"Прибыль: {profit}\n")
    
    @classmethod
    def total_branches(cls):
        #Возвращает количество филиалов компании
        return len(cls._branches)
    
    @classmethod
    def company_finances(cls):
        #Составление списка кортежей
        return [(branch.name, branch.revenue, branch.expenses) for branch in cls._branches]
    
    @classmethod
    def total_company_finances(cls):
        #Вычисление суммарных доходов и расходов всех филиалов
        total_revenue = sum(branch.revenue for branch in cls._branches)
        total_expenses = sum(branch.expenses for branch in cls._branches)
        return total_revenue, total_expenses  #Возвращение двух значений: общий доход и общие расходы
    
    @staticmethod
    def company_profit():
        #Использование метода total_company_finances для получения суммарных доходов и расходов
        total_revenue, total_expenses = Branch.total_company_finances()
        total_profit = total_revenue - total_expenses  #Прибыль всей компании
        #Возвращение состояния компании в зависимости от прибыли
        return f"Компания {'убыточна' if total_profit < 0 else 'прибыльна'}: {total_profit}"

branch1 = Branch("Филиал 1", 150, 2000000, 1000000) #Создание филиалов с названием "Филиал Х", Х сотрудниками, доходом Х и расходами Х
branch2 = Branch("Филиал 2", 50, 600000, 500000)
branch3 = Branch("Филиал 3", 140, 1500000, 1600000)

# Вывод информации о каждом филиале
print(branch1.present())
print(branch2.present())
print(Branch.total_branches())
print(Branch.company_finances())
print(Branch.total_company_finances())
print(Branch.company_profit())