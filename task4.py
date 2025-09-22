def create_digit_array(n):
    return [int(digit) for digit in str(n)]

def task1():
    n = int(input("Введите натуральное число N: "))

    # Проверка, что число натуральное
    if n <= 0:
        print("Пожалуйста, введите натуральное число (N > 0).")
    else:
        # Вызов функции и вывод результата
        digits = create_digit_array(n)
        print(f"Массив цифр числа {n}: {digits}")

def task2(x1, y1, x2, y2, x3, y3):
    area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2
    return area

def task3(N):
    def sum_digits(N):
        if N < 10:
            return N
        else:
            return N % 10 + sum_digits(N // 10)

    print(sum_digits(N))  # Выведет: 15

def main():
    #task1()
    #print(task2(1,2,3,4,5,6))
    task3(56)

main()