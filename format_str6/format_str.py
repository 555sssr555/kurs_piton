from matplotlib import pyplot as plt

input("""\t\t\tФорматирования строк!""")

img = plt.imread('/home/bsg/Desktop/shkola/Kurs_piton/format_str6/formati.png')
plt.imshow(img)
plt.show()

input("""Форматирование строк, это в какойто мере шаблон для подставки данных
y = input('Alex')
print('Hello, {}'.format(y))\t#В фигурные скобки поподает переменная Y
Hello, Alex
Если же в фигурные скобки установить индексацию с нуля, тогда
можно выберать куда какое значения пойдет {0}, {1} или на оборот.
name = input('Имя: ')
name: serg

surname = input('Фамилия: ')
surname: bob

year = int(input('Год: '))
year: 1647

print("Hello, {} {} {}".format(name, surname, year))
Hello, serg bob 1647

Распространенная 'f' строка которая записывается:
print(f'Hello, {name} {surname} {year}')
Hello, sergo bob 1647""")

img = plt.imread('/home/bsg/Desktop/shkola/Kurs_piton/format_str6/format.png')
plt.imshow(img)
plt.show()

img = plt.imread('/home/bsg/Desktop/shkola/Kurs_piton/format_str6/dop_met_ctr.png')
plt.imshow(img)
plt.show()

input("""Дополнительные функции в строках, их огромное количество,
расмотрим некоторые из них:
st = 'I_work_until_morning'
std = st.split('_')
print(std)
['I', 'work', 'until', 'morning']
далее join:
print(' '.join(std))
'I work until morning'
print(st.replace('o', 'O'))
I_wOrk_until_mOrning""")



