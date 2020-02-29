"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
school = [
          {"school_class":"5b","scores":[4,4,3,2,5,4,5]},
          {"school_class":"7a","scores":[5,4,2,2,3,4,2]},
          {"school_class":"8a","scores":[5,3,4,2,2,5,5]},
          {"school_class":"9b","scores":[2,5,5,5,5,3,5]},
          {"school_class":"10a","scores":[3,2,2,4,4,2,2]}
          ]
          
sum_class = 0
count_scores = 0
for clas in school: 
  sum_class += sum(clas['scores'])
  count_scores += len(clas['scores'])

  print(f"Средняя оценка класаа {clas['school_class']} : {sum(clas['scores'])/len(clas['scores'])} !")

print(f"Средняя оценка школы {sum_class/count_scores}!")
if __name__ == "__main__":
    main()
