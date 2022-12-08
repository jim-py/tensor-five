def check(num):
    try:
        num = int(num)
        if num < 0:
            print('Число должно быть положительным!')
            return False
        elif num == 0:
            print('Пусто!')
            return False
    except ValueError:
        print('Должно быть число!')
        return False
    return True


def fib_rec(N, f=[]):
    if len(f) < N:
        if len(f) < 1:
            f.append(0)
        elif len(f) < 2:
            f.append(1)
        else:
            f.append(f[-1] + f[-2])
        fib_rec(N)
        return f'{N}-ое число Фибоначчи - {f[N - 1]}'


n = input('Введите число: ')

if check(n):
    print(fib_rec(int(n)))
