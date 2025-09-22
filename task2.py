import math

def task1(x):
    if x<=3:
        return x*x-3*x+9
    else:
        return 1/(x*x*x + 1)

def task2(numbers):
    result = []
    for x in numbers:
        if x >= 0:
            result.append(x**2)
        else:
            result.append(x**4)
    return result

def task3(a,b,c,d):
    min1 = min(a, b)
    min2 = min(c, d)
    return max(min1, min2)

def task4(x,y):
    if x > y:
        return "x > y"
    else:
        return "x < y"

def task5(day_number):
    days = {
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота",
        7: "Воскресенье"
    }

    if 1 <= day_number <= 7:
        return "День недели:", days[day_number]
    else:
        return "Ошибка: номер дня должен быть от 1 до 7."

def main():
    print("task1")
    print(task1(4))
    print("task2")
    print(task2([2.0, -3.0, 0.5]))
    print("task3")
    print(task3(2,4,7, 6))
    print("task4")
    print(task4(2, 4))
    print("task5")
    print(task5(5))

main()
