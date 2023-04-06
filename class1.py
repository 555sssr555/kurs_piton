
privestvie1 = input("""Привет в этой программе будут проходить уроки
                    по языку програмировании на Python3 и так как это первый урок будет
                     много теории, но излагается эта теория в основном без
                     научных терминов.
                     Излогаться все будеть по тем соображениям которые я нашел
                     в пространстве интернет и так как я понемаю.
                     Теперь прост нажми энтэр 
                    """)
def clearShell():
    import os
    os.system(['clear', 'cls'][os.name == os.sys.platform])
clearShell()

import list_of_contents
class Imput_data:
    def __init__(name, lesson_number):
        _name = name
        lesson_number = lesson_number

    # def set_lessen_number(lesson_number):
    #     if lesson_number < 1 or lesson_number > 20:
    #         raise ValueError(f'Вы вели не существующий урок!')
    #     lesson_number = lesson_number



    def data_request():
         print(f' Привет {name} Ваш номер урока {lesson_number}')


if __name__ == '__main__':
    student = Imput_data(int(input(name, "Сделайте Ваш выбор: ")))
    student.data_request()



