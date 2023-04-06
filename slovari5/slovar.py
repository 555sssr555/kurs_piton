from matplotlib import pyplot as plt
import webbrowser
input("""\t\t\tСловари!""")

img = plt.imread('/home/bsg/Desktop/shkola/Kurs_piton/slovari5/slovari.png')
plt.imshow(img)
plt.show()

input("""Словари имеют ключ: значения.
с помощью словарей удобно описовать предметы, действия, значения и т.д и т.п
К примеру сеть wi-fi имеет названия TP-link_20 пароль 12345678 соотвественно
ключь TP-link_20 и значения ключа будет 12345678, запись таких значений следующим образом:
wlan = {"TP-link_20":"12345678", "Android":"543211234r", "Чашка":"Емкость которую 
используют в основном для наполнения жидкости"}
Можно вывести количество пар ключ-значения
for index in range(len(wlan)):
    print(index)
0
1
2
Это был цикл for который будет изучаться поздее.
Если нам нужно получить значения:
print(wlan['TP-link_20'])
12345678
Еще вариант:
print(wlan.get('Чашка'))
Емкость которую используют в основном для наполнения жидкости
Через гет можно добовлять ключ значения.
wlan['monitor']=wlan.get('monitor', 'Samsung')
print(wlan)
{'TP-link_20': '12345678', 'Android': '543211234r', 
'Чашка': 'Емкость которую используют в основном для наполнения жидкости', 
'monitor': 'Samsung'}""")

img = plt.imread('/home/bsg/Desktop/shkola/Kurs_piton/slovari5/slovari1.png')
plt.imshow(img)
plt.show()
img = plt.imread('/home/bsg/Desktop/shkola/Kurs_piton/slovari5/kluch_znachen.png')
plt.imshow(img)
plt.show()

webbrowser.get(using='firefox').open_new_tab('https://pythonworld.ru/osnovy/vstroennye-funkcii.html')


