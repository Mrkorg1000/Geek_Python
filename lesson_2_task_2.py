test_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(test_list))
test_list[:]
print(id(test_list))
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов

# функцию, которая определяет является элемент числом
def is_number(el):
    try:
        float(el)
        return True
    except ValueError:
        return False

# итерратор, дополняющий цифры нулём до двух целочисленных разрядов,
# если элемент - цифра и  дополняющий кавычки до и после цифры
# либо возвращающий элемент без изменеия (если не цифра):


def app_func():   # функция добавления в список кавычек, чтобы не было провторений в коде
    test_list_1.append('"')
    test_list_1.append(i)
    test_list_1.append('"')

test_list_1 = []
for i in test_list:
    if is_number(i):
        if '+' in i:
            i = '{:+03.0f}'.format(float(i))
            app_func()
        else:
            i = '{:02.0f}'.format(float(i))
            app_func()
    else:
        test_list_1.append(i)
print(f'test_list_1: {test_list_1}')


test_string = ' '.join(test_list_1)
print(f'test_string: {test_string}')