import webbrowser
from matplotlib import pyplot as plt
input("""\t\t\tКартэж!""")

img = plt.imread('/home/bsg/Desktop/shkola/Kurs_piton/kartegh4/kartedghi_tupl.png')
plt.imshow(img)
plt.show()

input("""Картежи нужны для набора не изменяемых данных. Чаще всего кортежи используются 
в функциях.
Но всеже в птоне можно практически все и одно из-практически есть метод добавить
в картеж список.
y = ['hello']
x = (1,2,3,4,5,y)
print(x)
(1, 2, 3, 4, 5, 'hello')
y.append('WORLD')
print(x)
(1, 2, 3, 4, 5, ['hello', 'WORLD'])""")

img = plt.imread('/home/bsg/Desktop/shkola/Kurs_piton/kartegh4/sozd_kart.png')
plt.imshow(img)
plt.show()

img = plt.imread('/home/bsg/Desktop/shkola/Kurs_piton/kartegh4/srezy.png')
plt.imshow(img)
plt.show()

img = plt.imread('/home/bsg/Desktop/shkola/Kurs_piton/kartegh4/mnogestva.png')
plt.imshow(img)
plt.show()

input("""Множества это унекальный набор значений, к примеру:
x = {1,2,54,2,543,2,2,2,2,2,3,3,4,4,53425,56, 'vova', 'vova'}
print(type(x), x)
<class 'set'> {1, 2, 3, 4, 53425, 54, 56, 'vova', 543}
Это обект который не содержит в себе дубликатов.
Ознакомтесь по ближе с возможностью типов данных 'set'""")

img = plt.imread('/home/bsg/Desktop/shkola/Kurs_piton/kartegh4/mnogestva1.png')
plt.imshow(img)
plt.show()

webbrowser.get(using='firefox').open_new_tab("https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html")
