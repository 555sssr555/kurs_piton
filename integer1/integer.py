
from matplotlib import pyplot as plt
import os

_tepe = input("""\t Целые числа.""")

img = plt.imread('/home/bsg/Desktop/shkola/Kurs_piton/integer1/png/celoy_number.png')
plt.imshow(img)
plt.show()
print("""Создадим перемкнную a  и присвоем ей значения 10 \n a = 10 \n и для того что проверить
тип данных есть такая функция 'type()', тоисть для просмотра типа данныч пишем 
'tepe' и в скобачки кладем переменную. Сделайте это прямо в терминале""")
def prov_():
    prov = input("Введите Ваш результат: ")
    if prov == "type(a)":
        print("Ведь нечиго сложного, правда?")
    else:
        prov_()
prov_()
input("Числа это не зменяемый тип данных")

def clearShell():
    import os
    os.system(['clear', 'cls'][os.name == os.sys.platform])
clearShell()

input("""Числа потдерживаю в принципе все математические операции.
a = 5
b = 10
print(a + b)
15
так же вычитания
print(a - b)
-5
-5 это отрицательное число""")

def clearShell():
    import os
    os.system(['clear', 'cls'][os.name == os.sys.platform])
clearShell()

input("""Пример с делением
a = 10
b = 5
print(a / b)
2.0
2.0 Это тип данных float иначе чистло с плавоющей запетой - только
в мосто запятой точка
Дальше деления на цело без остатка
print(a // b)
2
Даже если перезапишем переменую а
a = 12
print(a // b)
2
print(a / b)
2.4""")

def clearShell():
    import os
    os.system(['clear', 'cls'][os.name == os.sys.platform])
clearShell()

input("""Если же нужен только остаток от деления,
тогда нужен знак '%'
а = 17
b = 5
print(a % b)
2 
математические вычесления нам понабятся в дольнейшем
""")

img = plt.imread('/home/bsg/Desktop/shkola/Kurs_piton/integer1/png/obnovleniy_perem.png')
plt.imshow(img)
plt.show()

img = plt.imread('/home/bsg/Desktop/shkola/Kurs_piton/integer1/png/preobroz.png')
plt.imshow(img)
plt.show()

