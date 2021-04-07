# Задача 2
# Создать список, состоящий из кубов нечётных чисел от 0 до 1000
lst_1 = []
for number in range(1, 1001):
    if number % 2 != 0:
        lst_1.append(number ** 3)
print(f'lst_1: {lst_1}')


# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7

# функция, превращающая число в список цифр и вычисляющая сумму этих цифр

def lst_func(num):
    list_of_nums = []
    while num > 0:
        list_of_nums.append(num % 10)
        num = num // 10
    return sum(list_of_nums)


# Список чисел, сумма цифр которых делится нацело на 7
lst_for_sum = []
for el in lst_1:
    if lst_func(el) % 7 == 0:
        lst_for_sum.append(el)

print(f'lst_for_sum: {lst_for_sum}')

# Сумма чисел этого списка

print(f'Сумма элементов списка: {sum(lst_for_sum)}')

# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7. Внимание: новый список не создавать!!!
total = 0
for el in lst_1:
    el = el + 17
    if lst_func(el) % 7 == 0:
        total += el
print(f'Сумма элеменов нового списка: {total}')
