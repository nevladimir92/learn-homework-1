"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
QA = {"Как дела?":"Хорошо","Что делаешь?":"Програмирую", "Как погода?":"Гавно","Где работаешь?":"В кето","Будешь пиво?":"Да"}
while True:
    user_say = input("Введите вопрос..") 
    print(QA.get(user_say,"Давай другой вопрос"))
    





if __name__ == "__main__":
    ask_user()
