"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    """
    Замените pass на ваш код
    """
    while True:
      user_say = input("Как дела?...")
      if user_say == "Хорошо":
        break 
      else:
        print(f"{user_say}??? Не ври!!")
    
if __name__ == "__main__":
    ask_user()
