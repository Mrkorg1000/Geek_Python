# Функция определяющая склонение слово "процент" в зависимости от числа.

def ending(num):
    if 4 < num <= 20:
        print(f'{num} процентов')
    elif 2 <= num <= 4:
        print(f'{num} процента')
    elif num == 1:
        print(f'{num} процент')
    else:
        print('Программа работает только для чисел от 1 до 20')

# Проверка


for num in range(1, 21):
    ending(num)
