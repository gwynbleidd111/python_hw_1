#Задача 2___________________________________________________________

import math

x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))

result = math.sqrt((x2-x1)**2+(y2-y1)**2)

print(format(result,'.2f'))
