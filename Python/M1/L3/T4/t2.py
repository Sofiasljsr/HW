'''
Запросіть два числа a і b. 
Виведіть площу прямокутника із заданими сторонами в форматі, 
який вказаний в прикладі. 
Формула знаходження площі прямокутника: S = a * b. 
Приклад виводу результата S = 20, звертайте увагу на відступи між символами.
'''
num1 = input("Вкажіть число 1: ")
num2 = input("Вкажіть число 2: ")
s = int(num1) * int(num2)
print(f"S = {s}.")