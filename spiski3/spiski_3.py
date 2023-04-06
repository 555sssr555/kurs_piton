from matplotlib import pyplot as plt
input("""\t\t\tСписки!""")

def clearShell():
    import os
    os.system(['clear', 'cls'][os.name == os.sys.platform])
clearShell()

img = plt.imread('/home/bsg/Desktop/shkola/Kurs_piton/spiski3/spiski.png')
plt.imshow(img)
plt.show()

input("""Списки имеют возможность к изменяемости, 
их можно изменять и крутить как фантазии хватит
Для проверки меняется ли список, можно воспользоваться таким методом как 
'id'\t создадим переменную с списком
sp = [2, 4,1,87, 45, 0]
id.sp
140571588753728
добавим в список символы, пусть это будет слово
sp.append('films')
id(sp)
140571588753728
Идентичны
print(sp)
[2, 4, 1, 87, 45, 0, 'films']
Получения индекса всегда с помощью квадратных скобок
""")

img = plt.imread('/home/bsg/Desktop/shkola/Kurs_piton/spiski3/indeksaciy.png')
plt.imshow(img)
plt.show()

img = plt.imread('/home/bsg/Desktop/shkola/Kurs_piton/spiski3/operacii_spiski.png')
plt.imshow(img)
plt.show()

input("""Есть список 'sp' создадим еще олдин 's' и поработаем с ними
Обьеденяем списки
sp = [2, 4, 1, 87, 45, 0, 'films']
s = ['python3']
В переменную sp добавим s
print(sp.extend(s), sp)
None [2, 4, 1, 87, 45, 0, 'python3']
Вставка элемента через .insert()
sp.insert(0, 'number')
print(sp)
['number', 2, 4, 1, 87, 45, 0, 'films']
Удоления елемента по индексу с возвращением значения
ind = sp.pop(4)
print(ind, sp)
87 ['number', 2, 4, 1, 45, 0, 'films']

""")

img = plt.imread('/home/bsg/Desktop/shkola/Kurs_piton/spiski3/work_spisok.png')
plt.imshow(img)
plt.show()
