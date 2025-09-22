import math

def task1(x):
    d = x * x - 8 * x + 12
    if d == 0:
        return None
    return (x * x - 7 * x + 10) / d

def task2(x):
    d = 1 - math.cos(2 * x) + math.sin(2 * x)
    if d == 0:
        return None
    return (1 + math.cos(2 * x) + math.sin(2 * x)) / d

def distance(x1, y1, x2, y2): # сторона
    return math.hypot(x2 - x1, y2 - y1)

def triangle_perimeter(x1, y1, x2, y2, x3, y3): # периметр
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    return a + b + c

def triangle_area(x1, y1, x2, y2, x3, y3): #площадь
    area = 0.5 * abs(
        x1*(y2 - y3) +
        x2*(y3 - y1) +
        x3*(y1 - y2)
    )
    return area

def task3(x1, y1, x2, y2, x3, y3):
    a1 = (triangle_perimeter(x1, y1, x2, y2, x3, y3))
    a2 = (triangle_area(x1, y1, x2, y2, x3, y3))
    return a1, a2

def task4(A, B):
    if B <= 0:
        raise ValueError("B должно быть положительным")
    if A <= B:
        return 0  # на отрезок не помещается ни одного полного B
    return A // B  # целочисленное деление

def can_move(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

def task5(x1,x2,y1,y2):
    if can_move(x1, y1, x2, y2):
        return ("Конь может перейти за один ход.")
    else:
        return ("Конь НЕ может перейти за один ход.")

def main():
    print("task1")
    print(task1(1))
    print("task2")
    print(task2(2))
    print("task3")
    print(task3(1,1,2,2,3,4))
    print("task4")
    print(task4(8,2))
    print("task5")
    print(task5(8,2, 6,7))
main()
