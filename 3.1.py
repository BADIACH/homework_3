#def result (one_z, two_z):
 #   if result = one_z / two_z
#else:
#    result == 0
#    print('Вы поделили на нуль!!!')

#print(result (int(input('Введите первое число: '))), (int(input('Введите второе число: ')))
###я ебался с этим 2 часа
def divide(a, b):
    try:
        result =  a / b
    except ZeroDivisionError:
        return
    return result

try:
    one = float(input('a = '))
    two = float(input('b = '))
    print(f'a / b = {divide(one, two)}')
except ValueError:
    print('Деление на 0!!!')
