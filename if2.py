"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def Somestr(string_1,string_2):
  
  if  type(string_1) != str or type(string_2) != str:
   return 0
  if string_1 == string_2:
      return 1
  if string_1 != string_2 and len(str(string_1)) > len(str(string_2)):
      return 2
  if string_1 != string_2  and string_2 =='learn':
      return 3
  else:
      return 4
print(Somestr('lol',12))
print(Somestr('lol','lol'))
print(Somestr('lol','lol'))
print(Somestr('lol','learn'))


   
   ## В ней надо заменить pass на ваш код
   # """
    
    
if __name__ == "__main__":
    main()
