import sys
import math


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        while prompt != 1:
            print(prompt)
            coef_str = ''
            coef_str = input()
            for i in range(len(coef_str)):
                if coef_str[i] in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                    prompt = 1
                    break
            if prompt != 1:
                print("Введено не число, повторите попытку")
    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        if root > 0:
            result.append(root)
            result.append(math.sqrt(root))
            result.append(-1 * math.sqrt(root))
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 > 0:
            result.append(math.sqrt(root1))
            result.append(-1 * math.sqrt(root1))
        if root2 > 0:
            result.append(math.sqrt(root2))
            result.append(-1 * math.sqrt(root2))
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 2:
        print('Два корня: ', (roots[0], roots[1]))
    else:
        print('Корни: ', roots[0], roots[1], roots[2], roots[3])


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4
