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


num = input('Введите число: ')
check = True
try:
    num = int(num)
    if num < 0:
        check = False
        print('Число должно быть положительным!')
except ValueError:
    check = False
    print('Должно быть число!')

if check:
    print(fib_rec(num))
