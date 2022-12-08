def summa(*args):
    try:
        return f'Сумма чисел равна {sum(list(map(float, args[0].split())))}'
    except ValueError:
        return 'Должны быть только числа!'


print(summa(input('Введите числа: ')))
