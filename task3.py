import math

def area_base_height(base, height):
    return 0.5 * base * height

def area_two_sides_angle(a, b, angle_rad):
    return 0.5 * a * b * math.sin(angle_rad)

def area_three_sides(a, b, c):
    s = (a + b + c) / 2
    # Формула Герона
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def task1():
    while True:
        print("\nВыберите группу элементов треугольника:")
        print("1 - Основание и высота")
        print("2 - Две стороны и угол между ними (в радианах)")
        print("3 - Три стороны")
        print("0 - Выход")

        group = int(input("Введите номер группы: "))

        if group == 0:
            print("Программа завершена.")
            break
        elif group == 1:
            base = float(input("Введите основание: "))
            height = float(input("Введите высоту: "))
            area = area_base_height(base, height)
            print(f"Площадь треугольника: {area:.2f}")
        elif group == 2:
            a = float(input("Введите первую сторону: "))
            b = float(input("Введите вторую сторону: "))
            angle = float(input("Введите угол между сторонами (в радианах): "))
            area = area_two_sides_angle(a, b, angle)
            print(f"Площадь треугольника: {area:.2f}")
        elif group == 3:
            a = float(input("Введите первую сторону: "))
            b = float(input("Введите вторую сторону: "))
            c = float(input("Введите третью сторону: "))
            # Проверка, существует ли треугольник
            if a + b > c and a + c > b and b + c > a:
                area = area_three_sides(a, b, c)
                print(f"Площадь треугольника: {area:.2f}")
            else:
                print("Треугольник с такими сторонами не существует.")
        else:
            print("Некорректный номер группы. Попробуйте снова.")

def calculate_s(n):
    s = 0
    for i in range(n + 1):
        term = (-1) ** i * (1 / (2 ** i))
        s += term
    return s

def task2(n):
    if n <= 0:
        print("Пожалуйста, введите натуральное число (n > 0).")
    else:
        result = calculate_s(n)
        print(f"Сумма S для n = {n} равна: {result}")

def calculate_series_epsilon(epsilon):
    s = 0
    n = 1
    term = 1.0  # Первый член ряда
    while abs(term) >= epsilon:
        s += term
        n += 1
        term = (-1) ** (n - 1) / n
    return s, n - 1

def task3():
    # Заданная точность
    epsilon = 0.001

    # Вычисление суммы
    sum_result, terms = calculate_series_epsilon(epsilon)
    print(f"Сумма ряда с точностью {epsilon} = {sum_result}")
    print(f"Количество членов: {terms}")

def main():
    task3()


main()