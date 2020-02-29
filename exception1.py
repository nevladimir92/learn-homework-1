"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    QA = {"Как дела?":"Хорошо","Что делаешь?":"Програмирую", "Как погода?":"Гавно","Где работаешь?":"В кето","Будешь пиво?":"Да"}
    while True:
        try:
            user_say = input("Введите вопрос..") 
            print(QA.get(user_say,"Давай другой вопрос"))
            
        except KeyboardInterrupt:
           print("Пока!")
           break
if __name__ == "__main__":
    ask_user()
